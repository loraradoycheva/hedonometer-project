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



