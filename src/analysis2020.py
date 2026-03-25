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
api_key = "49DFgOqvegSUosGsqxBDnHu4ZmQ1pA6AhBS9YArVgrCteCMh"


QUERY = ""

BEGIN_DATE = "20200101"
END_DATE   = "20201231"

FQ = 'section.name:("World")'

SORT = "relevance" #requires further research

TIMEOUT = 60
SLEEP   = 12.5

CACHE_DIR = Path("data") / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

LIMIT = None          # None => as many as possible (still limited by MAX_PAGES and API caps)
MAX_PAGES = 100      # pages 0..99 (10 docs/page => up to ~1000 docs maximum)
REFRESH_MULTI = False

multi_cache = CACHE_DIR / "nyt_articlesearch_multi2020.json"

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

# remove timezone
df['pub_date'] = df['pub_date'].dt.tz_localize(None)

# keep only headline and date
df_clean = df[["headline", "pub_date"]].copy()

# remove empty headlines
df_clean = df_clean[df_clean["headline"] != ""]

# remove duplicates
df_clean = df_clean.drop_duplicates().reset_index(drop=True)

# save cleaned data
df_clean.to_csv("data/cache/nyt_headlines.csv", index=False)

