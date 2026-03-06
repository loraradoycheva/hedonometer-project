from pathlib import Path
import json
import pandas as pd


with open(Path("data")/("cache")/("2025")/"nyt_articlesearch_discuss_2025.json", "r", encoding="utf-8") as file:
    data = json.load(file)

df_discuss_25 = pd.json_normalize(data["docs"])

df_discuss_25["headline"] = df_discuss_25.get("headline.main", "").fillna("").astype(str).str.strip()

# Parse publication date
# - utc=True makes timezone explicit (NYT pub_date includes timezone info)
df_discuss_25["pub_date"] = pd.to_datetime(df_discuss_25.get("pub_date", None), errors="coerce", utc=True)

# Optional: build a richer text field for later NLP steps
df_discuss_25["abstract"] = df_discuss_25.get("abstract", "").fillna("").astype(str)
df_discuss_25["snippet"]  = df_discuss_25.get("snippet",  "").fillna("").astype(str)

# Combine into a single analysis string
# (This is a common NLP step: "build one text column")
df_discuss_25["text"] = (df_discuss_25["headline"] + " " + df_discuss_25["abstract"] + " " + df_discuss_25["snippet"]).str.strip()

# Dedupe: web_url is a good unique id for an article
df_discuss_25 = df_discuss_25.drop_duplicates(subset=["web_url"]).reset_index(drop=True)

(df_discuss_25[["pub_date", "headline", "web_url"]].head())

#print(df_discuss_25)
#df_discuss_25.to_csv('data/cache/2025/discuss_25.csv', index=False)
