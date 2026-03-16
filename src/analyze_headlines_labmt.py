"""
NYT Headline Analysis with labMT Happiness Lexicon
Loads headlines, tokenizes, counts frequencies, applies labMT happiness scores
"""

# ===== IMPORTS =====
import pandas as pd
import re
from collections import Counter
from pathlib import Path
import os

# ===== CONFIGURATION =====
YEAR = 2022  # <-- CHANGE TO YOUR YEAR
DATA_DIR = Path(".")

# ===== STOP WORDS =====
# Common English words to filter out
STOP_WORDS = set([
    'a', 'about', 'above', 'across', 'after', 'afterwards', 'again', 'against', 
    'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 
    'am', 'among', 'amongst', 'amoungst', 'amount', 'an', 'and', 'another', 
    'any', 'anyhow', 'anyone', 'anything', 'anyway', 'anywhere', 'are', 
    'around', 'as', 'at', 'back', 'be', 'became', 'because', 'become', 
    'becomes', 'becoming', 'been', 'before', 'beforehand', 'behind', 'being', 
    'below', 'beside', 'besides', 'between', 'beyond', 'bill', 'both', 
    'bottom', 'but', 'by', 'call', 'can', 'cannot', 'cant', 'co', 'computer',
    'con', 'could', 'couldnt', 'cry', 'de', 'describe', 'detail', 'do', 'done',
    'down', 'due', 'during', 'each', 'eg', 'eight', 'either', 'eleven', 'else',
    'elsewhere', 'empty', 'enough', 'etc', 'even', 'ever', 'every', 'everyone',
    'everything', 'everywhere', 'except', 'few', 'fifteen', 'fify', 'fill',
    'find', 'fire', 'first', 'five', 'for', 'former', 'formerly', 'forty',
    'found', 'four', 'from', 'front', 'full', 'further', 'get', 'give', 'go',
    'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 'hereafter',
    'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 'himself', 'his',
    'how', 'however', 'hundred', 'i', 'ie', 'if', 'in', 'inc', 'indeed',
    'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 'latter',
    'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 'meanwhile',
    'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 'move',
    'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never',
    'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor',
    'not', 'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once',
    'one', 'only', 'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours',
    'ourselves', 'out', 'over', 'own', 'part', 'per', 'perhaps', 'please',
    'put', 'rather', 're', 'same', 'see', 'seem', 'seemed', 'seeming', 'seems',
    'serious', 'several', 'she', 'should', 'show', 'side', 'since', 'sincere',
    'six', 'sixty', 'so', 'some', 'somehow', 'someone', 'something', 'sometime',
    'sometimes', 'somewhere', 'still', 'such', 'system', 'take', 'ten', 'than',
    'that', 'the', 'their', 'them', 'themselves', 'then', 'thence', 'there',
    'thereafter', 'thereby', 'therefore', 'therein', 'thereupon', 'these',
    'they', 'thick', 'thin', 'third', 'this', 'those', 'though', 'three',
    'through', 'throughout', 'thru', 'thus', 'to', 'together', 'too', 'top',
    'toward', 'towards', 'twelve', 'twenty', 'two', 'un', 'under', 'until',
    'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 'were', 'what',
    'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter', 'whereas',
    'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 'while',
    'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will',
    'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours',
    'yourself', 'yourselves',
    # Additional short words
    "'s", "'t", "'re", "'ve", "'m", "'ll", "'d",
    's', 't', 've', 'm', 'll', 'd',
    # Numbers
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
    'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth'
])

# ===== STEP 1: LOAD HEADLINES =====
print("=" * 70)
print(f"NYT HEADLINE ANALYSIS FOR {YEAR} WITH labMT HAPPINESS LEXICON")
print("=" * 70)

# Try multiple possible locations for the headlines file
headlines_file = f"nyt_{YEAR}_headlines.csv"
possible_paths = [
    headlines_file,                          # Current directory
    f"../{headlines_file}",                   # Parent directory
    f"/Users/annazuravel/Desktop/hedonometer-project-1/{headlines_file}"  # Full path
]

headlines_path = None
for path in possible_paths:
    if os.path.exists(path):
        headlines_path = path
        print(f"\nStep 1: Found headlines at: {path}")
        break

if headlines_path is None:
    print(f"\nStep 1: Could not find {headlines_file}")
    print("Looking for CSV files in current directory...")
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    print(f"Found: {csv_files}")
    if csv_files:
        headlines_path = csv_files[0]
        print(f"Using: {headlines_path}")
    else:
        exit()

# Load the headlines
df = pd.read_csv(headlines_path)
print(f"Loaded {len(df)} headlines")

# Clean up
df = df.dropna(subset=['headline'])
df = df[df['headline'].str.strip() != '']
df['pub_date'] = pd.to_datetime(df['pub_date'], errors='coerce')

print(f"Cleaned dataset: {len(df)} headlines")
print(f"Date range: {df['pub_date'].min().date()} to {df['pub_date'].max().date()}")

# Show sample
print("\nSample headlines:")
for i, row in df.head(5).iterrows():
    date_str = row['pub_date'].strftime('%Y-%m-%d') if pd.notna(row['pub_date']) else 'Unknown'
    headline = row['headline'][:80] + "..." if len(row['headline']) > 80 else row['headline']
    print(f"  {date_str}: {headline}")

# ===== STEP 2: LOAD labMT HAPPINESS LEXICON =====
print(f"\nStep 2: Loading labMT happiness lexicon...")

# Try multiple locations for labMT file
labmt_paths = [
    "labMT1.txt",
    "../labMT1.txt",
    "src/labMT1.txt",
    "/Users/annazuravel/Desktop/hedonometer-project-1/src/labMT1.txt"
]

labmt_file = None
for path in labmt_paths:
    if os.path.exists(path):
        labmt_file = path
        print(f"Found labMT at: {path}")
        break

if labmt_file is None:
    print("Could not find labMT1.txt")
    exit()

try:
    # Load the labMT data - it's tab-separated
    labmt_df = pd.read_csv(labmt_file, sep='\t')
    print(f"Loaded labMT lexicon with {len(labmt_df)} words")
    
    # Create happiness dictionary
    happiness_dict = dict(zip(
        labmt_df['word'].str.lower(),
        labmt_df['happs']
    ))
    
    print(f"Created happiness dictionary with {len(happiness_dict)} words")
    
except Exception as e:
    print(f"Error loading labMT file: {e}")
    exit()

# ===== STEP 3: TOKENIZE HEADLINES =====
print(f"\nStep 3: Tokenizing headlines into words...")

def tokenize_headline(text):
    """
    Convert headline to list of lowercase words
    Removes punctuation, keeps only alphabetic words
    """
    if not isinstance(text, str):
        return []
    
    # Convert to lowercase and find all alphabetic words
    words = re.findall(r'\b[a-z]+\b', text.lower())
    
    # REMOVE STOP WORDS - THIS IS THE KEY FIX
    words = [w for w in words if w not in STOP_WORDS and len(w) > 1]
    
    return words

# Apply tokenization
df['words'] = df['headline'].apply(tokenize_headline)

# Show example
print(f"\nExample headline: '{df['headline'].iloc[0]}'")
print(f"Tokenized (stop words removed): {df['words'].iloc[0]}")

# ===== STEP 4: COUNT WORD FREQUENCIES =====
print(f"\nStep 4: Counting word frequencies...")

# Collect all words
all_words = []
for word_list in df['words']:
    all_words.extend(word_list)

# Count frequencies
word_freq = Counter(all_words)

print(f"Total words (after removing stop words): {len(all_words):,}")
print(f"Unique words: {len(word_freq):,}")

# Show top 20 most frequent words
print("\nTop 20 most frequent words (stop words removed):")
print("-" * 50)
print(f"{'Word':<20} {'Frequency':<10}")
print("-" * 50)
for word, count in word_freq.most_common(20):
    print(f"{word:<20} {count:<10,}")

# ===== STEP 5: APPLY HAPPINESS SCORES =====
print(f"\nStep 5: Applying labMT happiness scores...")

scored_words = []
words_without_scores = []
word_stats = {'total': 0, 'scored': 0, 'unscored': 0}

for word, count in word_freq.most_common():
    word_stats['total'] += 1
    score = happiness_dict.get(word)
    
    if score is not None:
        scored_words.append({
            'word': word,
            'frequency': count,
            'happiness_score': score
        })
        word_stats['scored'] += 1
    else:
        words_without_scores.append(word)
        word_stats['unscored'] += 1

# Create DataFrame of scored words
scored_df = pd.DataFrame(scored_words)
scored_df = scored_df.sort_values('frequency', ascending=False)

print(f"\nWords found in labMT lexicon: {word_stats['scored']:,}")
print(f"Words not in lexicon: {word_stats['unscored']:,}")
print(f"Coverage: {word_stats['scored']/word_stats['total']*100:.1f}% of unique words")

# ===== STEP 6: DISPLAY TOP SCORED WORDS =====
print(f"\nTOP 20 WORDS BY FREQUENCY (with labMT happiness scores, stop words removed):")
print("-" * 80)
print(f"{'Word':<20} {'Frequency':<12} {'Happiness Score':<15} {'Sentiment':<15}")
print("-" * 80)

def get_sentiment_label(score):
    if score >= 7.0:
        return "Very Happy"
    elif score >= 6.0:
        return "Happy"
    elif score >= 5.0:
        return "Neutral"
    elif score >= 4.0:
        return "Sad"
    else:
        return "Very Sad"

for _, row in scored_df.head(20).iterrows():
    sentiment = get_sentiment_label(row['happiness_score'])
    print(f"{row['word']:<20} {row['frequency']:<12,} {row['happiness_score']:<15.2f} {sentiment}")

# ===== STEP 7: SHOW TOP WORDS BY HAPPINESS =====
print(f"\nTOP 10 HAPPIEST WORDS (min. 10 occurrences):")
print("-" * 70)
happiest = scored_df[scored_df['frequency'] >= 10].sort_values('happiness_score', ascending=False).head(10)
for _, row in happiest.iterrows():
    print(f"{row['word']:<20} Score: {row['happiness_score']:.2f}  (appears {row['frequency']:,} times)")

print(f"\nTOP 10 SADDEST WORDS (min. 10 occurrences):")
print("-" * 70)
saddest = scored_df[scored_df['frequency'] >= 10].sort_values('happiness_score', ascending=True).head(10)
for _, row in saddest.iterrows():
    print(f"{row['word']:<20} Score: {row['happiness_score']:.2f}  (appears {row['frequency']:,} times)")

# ===== STEP 8: SHOW WORDS MISSING FROM LEXICON =====
print(f"\nTOP 10 WORDS MISSING FROM labMT LEXICON:")
print("-" * 50)
missing_counts = [(word, word_freq[word]) for word in words_without_scores[:10]]
for word, count in missing_counts:
    print(f"{word}: {count:,} occurrences")

# ===== STEP 9: SAVE RESULTS =====
print(f"\nStep 9: Saving results...")

# Save scored words to CSV
output_file = f"nyt_{YEAR}_labmt_scored.csv"
scored_df.to_csv(output_file, index=False)
print(f"Saved scored words to: {output_file}")

# Save all word frequencies (for reference)
freq_df = pd.DataFrame([
    {'word': word, 'frequency': count}
    for word, count in word_freq.most_common()
])
freq_df.to_csv(f"nyt_{YEAR}_all_frequencies.csv", index=False)
print(f"Saved all frequencies to: nyt_{YEAR}_all_frequencies.csv")

# ===== FINAL SUMMARY =====
print("\n" + "=" * 70)
print(f"FINAL SUMMARY FOR {YEAR}")
print("=" * 70)
print(f"Total headlines: {len(df):,}")
print(f"Total words (after stop words removed): {len(all_words):,}")
print(f"Unique words: {len(word_freq):,}")
print(f"Words in labMT lexicon: {len(scored_df):,}")
print(f"Coverage: {len(scored_df)/len(word_freq)*100:.1f}%")
print(f"\nFiles created:")
print(f"   - {output_file} (main result - words with labMT scores)")
print(f"   - nyt_{YEAR}_all_frequencies.csv (all words with counts)")
print("=" * 70)

# Preview final output
print("\nPreview of final output (first 20 rows, stop words removed):")
print(scored_df.head(20).to_string(index=False))