import os, json, time, requests
from pathlib import Path
from datetime import date
import re
from collections import Counter
import matplotlib.pyplot as plt


import pandas as pd
import numpy as npgi



df = pd.read_csv('data/cache/2016/claim_16.csv')


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

# --- CHART 1: Most Frequent Words in NYT Headlines (2016) ---
top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20]
words, counts = zip(*top_words)

plt.figure(figsize=(12, 6))
plt.bar(words, counts, color='steelblue')
plt.title('Most Frequent Words in NYT World Headlines (2016)')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('figures/top_words_2016.png')
plt.close()
print("Chart 1 saved: top_words_2016.png")

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
print(f"Mean happiness score (2016): {df['happs_score'].mean():.3f}")

# --- CHART 2: Word Happiness vs Frequency ---
# Only include words that appear in both our corpus and the hedonometer
common_words = {w: c for w, c in word_counts.items() if w in happs_dict}
happs_scores = [happs_dict[w] for w in common_words]
frequencies  = [common_words[w] for w in common_words]

plt.figure(figsize=(10, 6))
plt.scatter(happs_scores, frequencies, alpha=0.5, color='steelblue')
plt.title('Word Happiness vs Frequency — NYT World Headlines (2016)')
plt.xlabel('Happiness Score (1=negative, 9=positive)')
plt.ylabel('Word Frequency in Corpus')
plt.tight_layout()
plt.savefig('figures/happiness_vs_frequency_2016.png')
plt.close()
print("Chart 2 saved: happiness_vs_frequency_2016.png")
