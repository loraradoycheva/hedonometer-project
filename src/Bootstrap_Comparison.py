import matplotlib.pyplot as plt
import numpy as np


years   = [2019, 2020, 2021, 2022, 2023, 2024, 2025]
means   = [5.1609, 5.2691, 5.2865, 5.2229, 5.1468, 5.1931, 5.1981]
ci_low  = [5.1305, 5.2433, 5.2609, 5.1961, 5.1083, 5.1666, 5.1686]
ci_high = [5.1916, 5.2922, 5.3117, 5.2490, 5.1857, 5.2192, 5.2276]


errors_low  = [m - l for m, l in zip(means, ci_low)]
errors_high = [h - m for h, m in zip(ci_high, means)]

plt.figure(figsize=(10, 6))
plt.errorbar(
    years, means,
    verterr=[errors_low, errors_high],
    fmt='o',
    color='steelblue',
    capsize=5,
    linewidth=2,
    markersize=8,
    label="Mean happiness (95% CI)"
)
#errorbar is function that draws points with error bars. Add downward and upward error in verterr
#format is circle 

plt.annotate("n=449", xy=(2023, 5.1468),
    xytext=(2023, 5.09),
    ha='center', fontsize=8, color='gray')

plt.title("Mean Happiness of NYT World Headlines 2019–2025\n"
          "(labMT hedonometer, bootstrap 95% CI, World section)")
plt.xlabel("Year")
plt.ylabel("Mean Happiness Score (labMT, 1–9 scale)")
plt.xticks(years) #for the x, make sure you use years as defined above
plt.ylim(5.05, 5.40) 
plt.grid(axis='y', alpha=0.3)
plt.legend() #shows the legend with label defined earlier
plt.tight_layout() #automatically adjusts spacing so labels titles etc don't get cutoff. 
plt.savefig("figures/happiness_over_time.png")
print("Saved to figures/happiness_over_time.png")