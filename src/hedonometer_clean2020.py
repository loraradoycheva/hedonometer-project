import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import json
from pathlib import Path

raw = json.loads(Path("data/cache/nyt_articlesearch_multi_2016_to_2021_not_1k.json").read_text(encoding="utf-8"))
#finds JSON file and reads is at text (utf-8) and loads converts it into python dictionary that the code can navigate. 
df = pd.json_normalize(raw["docs"])
#

hedonometer = pd.read_csv("data/labMT1.txt", sep="\t", comment="#")
hedonometer = hedonometer.replace("--", pd.NA)
hedonometer["happs"] = pd.to_numeric(hedonometer["happs"], errors="coerce")
happs_dict = dict(zip(hedonometer["word"], hedonometer["happs"]))

df["headline"] = df["headline.main"].fillna("").astype(str).str.strip()

def score_headline(text):
    words = text.lower().split()
    scores = [happs_dict[w] for w in words if w in happs_dict]
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

df["happs_score"] = df["headline"].apply(score_headline)

total = len(df)
scored = df["happs_score"].notna().sum()
print(f"Total headlines: {total}")
print(f"Scored headlines: {scored}")
print(f"Coverage: {scored/total*100:.1f}%")
print(f"Mean happiness score (2016-2021): {df['happs_score'].mean():.3f}")

scores = df["happs_score"].dropna().values
n = len(scores)
B = 2000
rng = np.random.default_rng(42)

boot_means = np.empty(B)
for b in range(B):
    resample = rng.choice(scores, size=n, replace=True)
    boot_means[b] = resample.mean()

ci_low = np.quantile(boot_means, 0.025)
ci_high = np.quantile(boot_means, 0.975)
point_estimate = scores.mean()

print(f"\n--- Bootstrap Results (2016-2021) ---")
print(f"Point estimate (mean happiness): {point_estimate:.4f}")
print(f"95% Bootstrap CI: [{ci_low:.4f}, {ci_high:.4f}]")
print(f"(Based on {B} resamples of n={n} scored headlines)")

plt.figure(figsize=(10, 5))
plt.hist(boot_means, bins=50, color="steelblue", edgecolor="white")
plt.axvline(ci_low,         color="red",   linestyle="--", label=f"CI low:  {ci_low:.4f}")
plt.axvline(ci_high,        color="red",   linestyle="--", label=f"CI high: {ci_high:.4f}")
plt.axvline(point_estimate, color="black", linestyle="-",  label=f"Mean:    {point_estimate:.4f}")
plt.title("Bootstrap Distribution of Mean Happiness Score\nNYT World Headlines 2016-2021")
plt.xlabel("Mean Happiness Score (from resam    pled headlines)")
plt.ylabel("Count (out of 2000 resamples)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/bootstrap_2016-2021.png")
plt.show()
print("\nFigure saved to figures/bootstrap_2016-2021.png")

Path("data/processed").mkdir(parents=True, exist_ok=True)
df[["headline", "happs_score"]].to_csv("data/processed/nyt_2016-2021_scored.csv", index=False)
print("Scored headlines saved to data/processed/nyt_2016-2021_scored.csv")
