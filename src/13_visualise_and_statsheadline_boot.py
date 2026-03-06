import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


df = pd.read_csv('data\cache\headlines_clean_scored_all.csv')


total = len(df)
scored = df["happs_score"].notna().sum()
print(f"Total headlines: {total}")
print(f"Scored headlines: {scored}")
print(f"Coverage: {scored/total*100:.1f}%")
print(f"Mean happiness score (2015-2025): {df['happs_score'].mean():.3f}")

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

print(f"\n--- Bootstrap Results (2015-2025) ---")
print(f"Point estimate (mean happiness): {point_estimate:.4f}")
print(f"95% Bootstrap CI: [{ci_low:.4f}, {ci_high:.4f}]")
print(f"(Based on {B} resamples of n={n} scored headlines)")

plt.figure(figsize=(10, 5))
plt.hist(boot_means, bins=50, color="steelblue", edgecolor="white")
plt.axvline(ci_low,         color="red",   linestyle="--", label=f"CI low:  {ci_low:.4f}")
plt.axvline(ci_high,        color="red",   linestyle="--", label=f"CI high: {ci_high:.4f}")
plt.axvline(point_estimate, color="black", linestyle="-",  label=f"Mean:    {point_estimate:.4f}")
plt.title("Bootstrap Distribution of Mean Happiness Score\nNYT World Headlines 2015-2025")
plt.xlabel("Mean Happiness Score (from resam    pled headlines)")
plt.ylabel("Count (out of 2000 resamples)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/bootstrap_2015-2025.png")
plt.show()
print("\nFigure saved to figures/bootstrap_2015-2025.png")

Path("data/processed").mkdir(parents=True, exist_ok=True)
df[["headline", "happs_score"]].to_csv("data/processed/nyt_2015-2025_scored.csv", index=False)
print("Scored headlines saved to data/processed/nyt_2015-2025_scored.csv")
