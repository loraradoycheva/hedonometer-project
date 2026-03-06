import os, json, time, requests
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
#import openpyxl



API = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

load_dotenv(find_dotenv())
api_key = os.getenv("NYT_API_KEY", "").strip()


if not api_key:
    raise ValueError(
        "Missing NYT_API_KEY. Put it in base.env like:\n"
        'NYT_API_KEY="YOUR_KEY_HERE"\n'
        "and restart/re-run the notebook."
    )


BEGIN_DATE = "20220101"
END_DATE   = "20221231"

FQ = '(headline.default:("discuss")) AND (section.name:"World")'

TIMEOUT = 60
SLEEP   = 12.5

CACHE_DIR = Path("data") / "cache"
CACHE_DIR.mkdir(parents=True, exist_ok=True)

LIMIT = 100
MAX_PAGES = 100
REFRESH_MULTI = False

multi_cache = CACHE_DIR / "nyt_articlesearch_discuss_2022.json"

if (not REFRESH_MULTI) and multi_cache.exists() and multi_cache.stat().st_size > 0:
    result_multi = json.loads(multi_cache.read_text(encoding="utf-8"))
    source = "cache"
else:
    base_params = {
        "api-key": api_key,
        "begin_date": BEGIN_DATE,
        "end_date": END_DATE
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

#df['pub_date'] = df['pub_date'].dt.tz_localize(None) #THIS IS OPTIONAL IF YOU WANT TO REVIEW THE DATA MANUALLY
#df.to_excel("test_report_2016.xlsx") #THIS IS OPTIONAL IF YOU WANT TO REVIEW THE DATA MANUALLY