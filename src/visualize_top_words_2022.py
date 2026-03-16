import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load your data
df = pd.read_csv('nyt_2022_labmt_scored.csv')
top_words = df.head(20)

# Create horizontal bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# Create bars
y_pos = np.arange(len(top_words))
bars = ax.barh(y_pos, top_words['frequency'])

# Customize colors based on happiness score
for i, (bar, score) in enumerate(zip(bars, top_words['happiness_score'])):
    if score >= 7:
        bar.set_color('darkgreen')
    elif score >= 6:
        bar.set_color('lightgreen')
    elif score >= 5:
        bar.set_color('gray')
    elif score >= 4:
        bar.set_color('orange')
    else:
        bar.set_color('red')

# Add labels
ax.set_yticks(y_pos)
ax.set_yticklabels(top_words['word'])
ax.set_xlabel('Frequency')
ax.set_title('Top 20 Words in NYT Headlines (2022)\nColored by Happiness Score', fontsize=14)

# Add frequency labels on bars
for i, (bar, freq) in enumerate(zip(bars, top_words['frequency'])):
    ax.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2, 
            str(freq), va='center')

# Add legend for colors
from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='darkgreen', label='Very Happy (7-9)'),
    Patch(facecolor='lightgreen', label='Happy (6-7)'),
    Patch(facecolor='gray', label='Neutral (5-6)'),
    Patch(facecolor='orange', label='Sad (4-5)'),
    Patch(facecolor='red', label='Very Sad (1-4)')
]
ax.legend(handles=legend_elements, loc='lower right')

plt.tight_layout()
plt.savefig('nyt_2022_top_words_colored.png', dpi=300, bbox_inches='tight')
plt.show()