from pathlib import Path
import os
import json
import time
import requests
from datetime import date
import re
from collections import Counter
from dotenv import load_dotenv  # Uncommented and fixed

import pandas as pd
import numpy as np
import openpyxl

# ===== LOAD API KEY FROM .ENV =====
load_dotenv()  # This loads your .env file
api_key = os.getenv('NYT_API_KEY')  # Gets your key from .env

if not api_key:
    raise ValueError("""
    ⚠️ API key not found! 
    
    Please make sure:
    1. You have a .env file in your project root
    2. The .env file contains: NYT_API_KEY=your_actual_key_here
    3. There are no spaces around the =
    """)

# ===== CONFIGURATION =====
API = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

# Set your year here (change this!)
YEAR = 2022  # <-- CHANGE THIS TO YOUR YEAR
BEGIN_DATE = f"{YEAR}0101"  # Automatically set to Jan 1
END_DATE = f"{YEAR}1231"    # Automatically set to Dec 31

QUERY = ""
FQ = ""  # Empty = no filter (get all sections)
# FQ = 'section.name:("World")'  # Uncomment if you want only World section

SORT = "newest"  # "newest" or "relevance" or "oldest"

TIMEOUT = 60
SLEEP = 12.5  # Be polite to API (6 requests per minute max)

# ===== CACHE SETUP =====
CACHE_DIR = Path("data") / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

LIMIT = None  # None => as many as possible (max 1000 due to API)
MAX_PAGES = 100  # pages 0..99 (10 docs/page => up to ~1000 docs)
REFRESH_MULTI = False  # Set to True to force fresh download

multi_cache = CACHE_DIR / f"nyt_{YEAR}_articlesearch.json"

print("=" * 60)
print(f"📰 NYT ARTICLE FETCHER FOR {YEAR}")
print("=" * 60)
print(f"✅ API key loaded: {api_key[:5]}...{api_key[-5:]}")
print(f"📅 Date range: {BEGIN_DATE} to {END_DATE}")
print(f"📁 Cache file: {multi_cache}")
print("=" * 60)

# ===== FETCH OR LOAD FROM CACHE =====
if (not REFRESH_MULTI) and multi_cache.exists() and multi_cache.stat().st_size > 0:
    print("📂 Loading from cache...")
    result_multi = json.loads(multi_cache.read_text(encoding="utf-8"))
    source = "cache"
    print(f"✅ Loaded {result_multi.get('count', 0)} articles from cache")
else:
    print("🌐 Fetching from NYT API...")
    base_params = {
        "api-key": api_key,
        "q": QUERY,
        "begin_date": BEGIN_DATE,
        "end_date": END_DATE,
        "sort": SORT,
    }
    if FQ:
        base_params["fq"] = FQ

    docs = []
    hits = None
    source = "api"

    for page in range(MAX_PAGES):
        print(f"  Fetching page {page}...", end="")
        
        params = dict(base_params)
        params["page"] = page

        try:
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

            if hits is None:
                hits = meta.get("hits")
                print(f" total matches in database: {hits}")

            if not page_docs:
                print(" No more articles")
                break

            docs.extend(page_docs)
            print(f" ✓ Got {len(page_docs)} articles (total: {len(docs)})")

            if LIMIT is not None and len(docs) >= LIMIT:
                docs = docs[:LIMIT]
                print(f"✓ Reached limit of {LIMIT} articles")
                break

            time.sleep(SLEEP)

        except requests.exceptions.RequestException as e:
            print(f" ❌ Error: {e}")
            break

    result_multi = {
        "source": "articlesearch",
        "params": base_params,
        "hits": hits,
        "count": len(docs),
        "docs": docs,
    }

    # Save to cache
    multi_cache.write_text(
        json.dumps(result_multi, ensure_ascii=False, indent=2), 
        encoding="utf-8"
    )
    print(f"✅ Saved {len(docs)} articles to cache")

print("=" * 60)
print(f"📊 Total articles retrieved: {result_multi.get('count', 0)}")
print(f"📊 Total matches in database: {result_multi.get('hits', 'unknown')}")

# ===== CREATE DATAFRAME =====
print("\n📋 Creating DataFrame...")
df_multi = pd.json_normalize(result_multi["docs"])
df = df_multi.copy()

# Extract headline
df["headline"] = df.get("headline.main", "").fillna("").astype(str).str.strip()

# Parse publication date
df["pub_date"] = pd.to_datetime(df.get("pub_date", None), errors="coerce", utc=True)

# Optional fields
df["abstract"] = df.get("abstract", "").fillna("").astype(str)
df["snippet"] = df.get("snippet", "").fillna("").astype(str)
df["text"] = (df["headline"] + " " + df["abstract"] + " " + df["snippet"]).str.strip()

# Remove duplicates
df = df.drop_duplicates(subset=["web_url"]).reset_index(drop=True)

# Remove timezone for easier viewing
df['pub_date'] = df['pub_date'].dt.tz_localize(None)

# ===== SAVE FILES =====
print("\n💾 Saving files...")

# Save full Excel file
excel_file = f"nyt_{YEAR}_full_data.xlsx"
df.to_excel(excel_file, index=False)
print(f"✅ Full data saved to: {excel_file}")

# Save just headlines for your analysis
headlines_file = f"nyt_{YEAR}_headlines.csv"
df[['pub_date', 'headline']].to_csv(headlines_file, index=False)
print(f"✅ Headlines only saved to: {headlines_file}")

# ===== PREVIEW =====
print("\n📰 Sample headlines:")
print("-" * 60)
for i, row in df[['pub_date', 'headline']].head(10).iterrows():
    date_str = row['pub_date'].strftime('%Y-%m-%d') if pd.notna(row['pub_date']) else 'No date'
    headline = row['headline'][:70] + "..." if len(row['headline']) > 70 else row['headline']
    print(f"{date_str}: {headline}")

print("=" * 60)
print(f"\n✅ Done! Total articles: {len(df)}")
print(f"📁 Files created:")
print(f"   - {excel_file} (all data)")
print(f"   - {headlines_file} (headlines only)")
print(f"   - {multi_cache} (cached JSON)")