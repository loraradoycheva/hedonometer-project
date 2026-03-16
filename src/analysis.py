from pathlib import Path
import os, json, time, requests
from datetime import date
import re
from collections import Counter
#dotenv import load_dotenv NOT IMPORTANT NOW

import pandas as pd
import numpy as np

import openpyxl




API = "https://api.nytimes.com/svc/search/v2/articlesearch.json"
api_key = "beprTHgUtEwPUQZZXyrAsGAR4gprARlizSSkyJgOxA1HywXE"


QUERY = ""

BEGIN_DATE = "20190101"
END_DATE   = "20191231"

FQ = 'section.name:("World")'

SORT = "relevance" #requires further research

TIMEOUT = 60
SLEEP   = 12.5

CACHE_DIR = Path("data") / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

LIMIT = None          # None => as many as possible (still limited by MAX_PAGES and API caps)
MAX_PAGES = 100      # pages 0..99 (10 docs/page => up to ~1000 docs maximum)
REFRESH_MULTI = False
multi_cache = CACHE_DIR / "nyt_articlesearch_multi.json"

if (not REFRESH_MULTI) and multi_cache.exists() and multi_cache.stat().st_size > 0:
    result_multi = json.loads(multi_cache.read_text(encoding="utf-8"))
    source = "cache"
else:
    base_params = {
        "api-key": api_key,
        "q": QUERY,
        "begin_date": BEGIN_DATE,
        "end_date": END_DATE,
        "sort": SORT,
    }
    if FQ:
        base_params["fq"] = FQ

    docs = []          # all documents we collect across pages
    hits = None        # total matches for query (reported by NYT)
    source = "api"

    for page in range(MAX_PAGES):
        # Copy base params and add the page number
        params = dict(base_params)
        params["page"] = page

        r = requests.get(
            API,
            params=params,
            timeout=TIMEOUT,
            headers={"User-Agent": "NYTNotebook/1.0 (+https://developer.nytimes.com)"},
        )
        r.raise_for_status()
        data = r.json()

        response = data.get("response") or {}
        meta = response.get("meta") or {}
        page_docs = response.get("docs") or []

        # hits is total matches for the query across all pages
        if hits is None:
            hits = meta.get("hits")

        # If the API gives us no docs, there are no more pages to fetch
        if not page_docs:
            print(f"Stopped: page {page} returned 0 docs.")
            break

        docs.extend(page_docs)

        # If we have a LIMIT, stop once we have enough
        if LIMIT is not None and len(docs) >= LIMIT:
            docs = docs[:LIMIT]
            print(f"Stopped: reached LIMIT={LIMIT} docs.")
            break

        # Sleep between requests to avoid rate limit problems
        time.sleep(SLEEP)

    result_multi = {
        "source": "articlesearch",
        "params": base_params,
        "hits": hits,
        "count": len(docs),
        "docs": docs,
    }

    # Cache for fast re-runs
    multi_cache.write_text(json.dumps(result_multi, ensure_ascii=False, indent=2), encoding="utf-8")

#print("multi-page source:", source)
#print("multi-page cache:", multi_cache)
#print("hits (total matches):", result_multi.get("hits"), "| downloaded:", result_multi.get("count"))

#print(json.dumps(result_multi, indent=2, sort_keys=True)[:4000], "\n...\n(truncated)")

df_multi = pd.json_normalize(result_multi["docs"])
df = df_multi.copy()


df["headline"] = df.get("headline.main", "").fillna("").astype(str).str.strip()

# Parse publication date
# - utc=True makes timezone explicit (NYT pub_date includes timezone info)
df["pub_date"] = pd.to_datetime(df.get("pub_date", None), errors="coerce", utc=True)

# Optional: build a richer text field for later NLP steps
df["abstract"] = df.get("abstract", "").fillna("").astype(str)
df["snippet"]  = df.get("snippet",  "").fillna("").astype(str)

# Combine into a single analysis string
# (This is a common NLP step: "build one text column")
df["text"] = (df["headline"] + " " + df["abstract"] + " " + df["snippet"]).str.strip()

# Dedupe: web_url is a good unique id for an article
df = df.drop_duplicates(subset=["web_url"]).reset_index(drop=True)

(df[["pub_date", "headline", "web_url"]].head())

df['pub_date'] = df['pub_date'].dt.tz_localize(None) #THIS IS OPTIONAL IF YOU WANT TO REVIEW THE DATA MANUALLY

df.to_excel("testing.xlsx") #THIS IS OPTIONAL IF YOU WANT TO REVIEW THE DATA MANUALLY


import matplotlib.pyplot as plt
from collections import Counter

# Load hedonometer lexicon
# labMT1.txt contains ~10,000 words rated for happiness (1-9 scale)
hedonometer = pd.read_csv('data/labMT1.txt', sep='\t', comment='#')
hedonometer = hedonometer.replace('--', pd.NA)
hedonometer['happs'] = pd.to_numeric(hedonometer['happs'], errors='coerce')

# Create a dictionary: word -> happiness score
happs_dict = dict(zip(hedonometer['word'], hedonometer['happs']))

# --- STEP 1: Count word frequencies across all headlines ---
# We tokenize (split into words) and lowercase for consistency
all_words = []
for headline in df['headline']:
    words = headline.lower().split()
    all_words.extend(words)

word_counts = Counter(all_words)

# Stop words: common neutral words
stop_words = {'the', 'a', 'an', 'in', 'of', 'to', 'and', 
              'for', 'on', 'at', 'is', 'as', 'by', 'with', 
              'from', 'that', 'it', 'its', 'are', 'was', 'after', 'hong', 'kong'}

# Only keep words that are IN the hedonometer lexicon
# Methodological choice: if a word has no happiness score, 
# it's not relevant to our analysis
word_counts = {w: c for w, c in word_counts.items() 
               if w not in stop_words 
               and w in happs_dict  # only hedonometer words!
               and len(w) > 2}

print(f"\nUnique words found in hedonometer: {len(word_counts)}")

# --- CHART 1: Most Frequent Words in NYT Headlines (2019) ---
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20]
words, counts = zip(*top_words)

plt.figure(figsize=(12, 6))
plt.bar(words, counts, color='steelblue')
plt.title('Most Frequent Words in NYT World Headlines (2019)')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figures/top_words_2019.png')
plt.close()
print("Chart 1 saved: top_words_2019.png")

# --- STEP 2: Score each headline using hedonometer ---
# Methodological choice: we ignore words not in the lexicon
# and report coverage (how many words matched)
def score_headline(text):
    words = text.lower().split()
    scores = [happs_dict[w] for w in words if w in happs_dict]
    if len(scores) == 0:
        return None  # return None if no words matched
    return sum(scores) / len(scores)

df['happs_score'] = df['headline'].apply(score_headline)

# Report coverage
total_headlines = len(df)
scored_headlines = df['happs_score'].notna().sum()
print(f"Coverage: {scored_headlines}/{total_headlines} headlines scored")
print(f"Mean happiness score (2019): {df['happs_score'].mean():.3f}")

# --- CHART 2: Word Happiness vs Frequency ---
# Only include words that appear in both our corpus and the hedonometer
common_words = {w: c for w, c in word_counts.items() if w in happs_dict}
happs_scores = [happs_dict[w] for w in common_words]
frequencies  = [common_words[w] for w in common_words]

plt.figure(figsize=(10, 6))
plt.scatter(happs_scores, frequencies, alpha=0.5, color='steelblue')
plt.title('Word Happiness vs Frequency — NYT World Headlines (2019)')
plt.xlabel('Happiness Score (1=negative, 9=positive)')
plt.ylabel('Word Frequency in Corpus')
plt.tight_layout()
plt.savefig('figures/happiness_vs_frequency_2019.png')
plt.close()
print("Chart 2 saved: happiness_vs_frequency_2019.png")
