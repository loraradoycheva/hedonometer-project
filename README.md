# hedonometer-project
# Dataset
The dataset used is labMT 1.0 (language assessment by Mechanical Turk), 
from Dodds et al. (2011). It contains happiness scores for 10,222 words, 
rated by workers on Amazon Mechanical Turk on a scale from 1 to 9.

The file was loaded as a tab-delimited text file, skipping comment lines 
starting with #. Missing values (--) were replaced with NaN. 
The dataset has 10,222 rows and 9 columns.

# Data Dictionary
- **word** — the English word being rated. Type: text. No missing values.
- **rank** — overall frequency rank across all corpora. Type: integer. No missing values.
- **happs** — average happiness score (scale 1–9). Type: float. No missing values.
- **stddev** — standard deviation of happiness ratings (how much raters disagreed). Type: float. No missing values.
- **rank.1** — frequency rank in Twitter. Type: float. 5192 missing values (word not in top 5000).
- **rank.2** — frequency rank in Google Books. Type: float. 5192 missing values.
- **rank.3** — frequency rank in New York Times. Type: float. 5192 missing values.
- **rank.4** — frequency rank in Music Lyrics. Type: float. 5192 missing values.

A missing rank means the word did not appear in the top 5000 most frequent 
words in that corpus.

# Sanity Checks
No duplicate rows were found. A random sample of 5 words (agent, doesn't, 
variables, stem, pillow) showed mid-range happiness scores between 5.0 and 6.9 — 
nothing unexpected. The 10 happiest words included laughter, happiness, love and joy, 
while the 10 saddest included suicide, terrorism, murder and cancer. 
Both lists match what you would intuitively expect.

# Histogram of happiness score (figures/histogram_happs.png)
The histogram shows that most words in the labMT dataset score around 5 on the 
happiness scale, with a mean of 5.37 and a median of 5.44. The distribution is 
roughly bell-shaped but slightly skewed to the left, meaning there are more words 
trailing off toward the sad end than the happy end. The middle 90% of words fall 
between scores of 3.18 and 7.08, suggesting that truly extreme words are relatively rare.

# Scatterplot of happiness vs standard deviation (figures/scatter_happs_stddev.png)
The scatterplot shows that the most contested words tend to cluster around the middle happiness scores rather than at the extremes. 
Words like "whiskey" and "cigarettes" are contested because people associate them with both 
pleasure and addiction. "Churches" and "capitalism" are politically and culturally divisive, 
meaning people's backgrounds strongly influence how they rate them. "Mortality" sits in the 
middle because it can feel clinical and neutral to some, but deeply distressing to others.

# 5000 most common words, similar or different?
We have four corpora: Twitter, Google Books, NYT, and Lyrics. Each one has its own list of the 5000 most common words.
We want to know: do these four lists contain the same words, or different words. 
rank 1 = twitter
rank 2 = Google Books
rank 3 = NYT
rank 4 = Lyrics
e.g. love: rank.4 = 5, means love is ranked 5th most commmon in Lyrics. 

To answer this, we compare the lists with each other. 
How many words appear in BOTH Twitter and Google Books?
How many words appear in BOTH Google Books and NYT?
How many words appear in ALL FOUR at the same time?
The more words two corpora share, the more similar their vocabulary is. The fewer words they share, the more different they are.
We then draw a bar chart to visualize these overlaps so it's easy to see which corpora are most similar to each other.

Every ranklist has 519 2 words missing, because only the top 5000 words are being ranked in each ranklist. The total amount of words evaluated for happiness scores is 10192. Therefore every ranklist misses 10192 - 5000 = 5192. This means every word that has a rank in one of the platforms, appears in the happiness rated words. 

Step 1: Find which words are missing from each corpus and check if the same words are missing everywhere
Step 2: Count how many words the corpora have in common with each other
Step 3: Draw a bar chart showing those overlaps


## 2019 Analysis

### Data
- 1000 NYT World section headlines from 2019
- Fetched via NYT Article Search API

### Method
- Scored headlines using the labMT hedonometer lexicon (10,000 words rated 1-9)
- Removed stop words and words not in the hedonometer lexicon
- Words like 'hong' and 'kong' were manually excluded as they appear only as 
  part of 'Hong Kong' and their hedonometer scores are misleading

### Results
- Mean happiness score: **5.161** (scale 1-9, 5=neutral)
- 1000/1000 headlines successfully scored
- Most frequent emotional words: new, says, police, protests, election, killed
