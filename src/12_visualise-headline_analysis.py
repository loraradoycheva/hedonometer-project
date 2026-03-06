from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
sns.set_style("whitegrid")


df = pd.read_csv('data/cache/2025/data_2025.csv')


# Load hedonometer lexicon
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
stop_words = set(ENGLISH_STOP_WORDS)

# Only keep words that are IN the hedonometer lexicon
# Methodological choice: if a word has no happiness score, 
# it's not relevant to our analysis
word_counts = {w: c for w, c in word_counts.items() 
               if w not in stop_words 
               and w in happs_dict  # only hedonometer words!
               and len(w) > 2}

print(f"\nUnique words found in hedonometer: {len(word_counts)}")



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
print(f"Mean happiness score (2025): {df['happs_score'].mean():.3f}")

# --- CHART: Word Happiness vs Frequency and Top Words ---
common_words = {w: c for w, c in word_counts.items() if w in happs_dict}
happs_scores = [happs_dict[w] for w in common_words]
frequencies  = [common_words[w] for w in common_words]

top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:25]
words, counts = zip(*top_words)


fig, ax = plt.subplots(nrows=1, ncols=2, gridspec_kw={'width_ratios': [1.5, 1]}, figsize=(30,10))
#plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
sns.scatterplot(x=happs_scores, y=frequencies, edgecolor="None", alpha=0.5, s=35, ax=ax[0])
ax[0].set_title('Word Happiness vs Frequency — NYT World Headlines (2025)', fontsize=18)
ax[0].set_xlabel('Happiness Score (1=negative, 9=positive)', fontsize=13)
ax[0].set_ylabel('Word Frequency in Corpus', fontsize=13)

sns.barplot(x=words, y=counts, ax=ax[1])
plt.xticks(rotation=60)
ax[1].tick_params(axis='both', labelsize=10)
ax[1].set_title('Most Frequent Words in NYT World Headlines (2025)', fontsize=18)
ax[1].set_xlabel(' ')
ax[1].set_ylabel('Frequency', fontsize=13)

plt.tight_layout(pad=7, w_pad=5, h_pad=0.5)


#plt.savefig('figures/composite_words_2025.png')

#plt.show()
