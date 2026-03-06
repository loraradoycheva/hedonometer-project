# Seminars 3 & 4 — Hedonometer Project

This folder provides project structure and demo script for the Seminars 3 & 4 group project stage using the **labMT 1.0** dataset (Data Set S1 from the Hedonometer paper).

It includes:
- the labMT 1.0 dataset file (`data/raw/Data_Set_S1.txt`)
- a runnable demo analysis script (`src/hedonometer_labmt_demo.py`) that produces a *typical* set of outputs aligned to the assignment
- course documents in `docs/` (original paper + paper companion + assignment + project quickstart), provided as **.pdf**

## Folder layout (course convention)

- `src/` — Python scripts you run
- `data/raw/` — input data (treat as read-only)
- `figures/` — PNG plots (embed these in your GitHub README)
- `tables/` — CSV tables/summaries (optional to embed, but useful for analysis)
- `docs/` — assignment + paper companion + quickstart handout

## Setup + run (from the project root)

### 1. Create a virtual environment

**macOS / Linux**
```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip
```

**Windows (PowerShell)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
py -m pip install --upgrade pip
```

### 2) Install dependencies
```bash
python3 -m pip install -r requirements.txt
```

### 3) Run the demo analysis
```bash
python3 src/run_analysis.py
```

### What gets generated?
After running, look in:
- `figures/` — PNG plots
- `tables/` — CSV summary tables

### HEDONOMETER PROJECT
This project is set to analyze the labMT1.0 dataset, that assigns happiness scores to common english words. The scores are based on human ratings. With Python, we are able to clean and explore the dataset, focusing on words usage across different corpora. With this dataset, we are also able to critically reflect on the limitations and design of the study. 

### 1.1 Dataset Origin
This dataset was loaded from a file using pandas. The metadata lines on top of the file were skipped with the import, and `--` values were treated as missing values. 

This dataset contains 10223 rows and 8 columns. Each row represents a single English word and columns contain information such as frequency usage across different corpora, the vatiation of ratings across different annotators and happiness score. 

The missing rank `--` means that the word does not appear in the list for that specific corpus.

### 1.2 Data Dictionary
- `word` - the english word that is being rated
  (type: string, no missing values)
- `rank` - placement of the word in the dataset
  (type: integer, no missing values)
- `happs` -  happiness rating on a scale from 1-9
  (type: float, no missing values)
- `stddev` - the vatiation of ratings across different annotators
  (type: float, no missing values)
- `rank.1` - frequency on twitter
  (type: float, values are missing)
- `rank.2` - frequency on google
  (type: float, values are missing)
- `rank.3` - frequency in NYT articles
  (type: float, values are missing)
- `rank.4` - frequency in lyrics
  (type: float, values are missing)

Some rank columns are represented as floats instead of integers in pandas to accomodate their missing values.

### 1.3 Methods - Sanity Checks
There were several checks performed in the code to verify whether the dataset is loaded correctly and well structured.

Firstly, we checked if any rows were duplicated. We got a result that there were `0` duplicated rows, meaning that each of the words appeared only once in the dataset. 

Our next step was to perform a check on a random sample of the word set to see if each column has appropiate values. This confirmed that each of the rows contains a `word`, `happs` and `stddev`. Some values were missinng but they were appearing as `NaN` which is correct in this form. 

At the last, we checked the words with the highest and lowest ranking. The most positive words were `laughter`, `happiness`, `love`, `happy` or `joy` and scored 8.0 on happs. Examples of negative words include `suicide`, `cancer`, `kill`, `rape` or `murder` and they scored closely to 1.3 - 1.5. 

These words corresponded to our expectations. What makes those sanity checks interesting is the fact that happs generaly reflects shared interpretation rather than objective truth, as the scores are just a subjective judgments of the words. 

### 2.1 Distribution of happiness scores

The Distribution of Happiness histogram is slightly left skewed, with its mean (at 5.38) infinitesimally smaller than the median (at 5.44). It features a longer, slowly ascending left tail in comparison to its steeper and shorter right one, a pattern which repeats when examining the curves of Kernel Density Estimates (KDE) for each corpus; although the Google Books and NYT curves show a higher density of words when approaching the score of 6 than NYT and Twitter. When comparing the box plots for each corpus, we can also see that the Google Books corpus has the highest mean and median distribution of happiness, followed closely by NYT, then Twitter and with the mean and median of the Music Lyrics coming closest (exact values tbd) to the general values. At the same time, Google Books corpus has, seemingly, the highest negative outlier count out of all four corpuses, though the precise count is currently unknown and could be disputed by the Comparative KDE plot.

Though the difference is minimal, it is unexpected that the highest density of the more negatively scored words, as evidenced by the bump in its KDE curve between values of 2 and 4, belongs to Music Lyrics rather than Twitter. It could potentially be explained by the timeframe during which the dataset was put together, when Twitter was still a relatively new platform and still establishing its vernacular.

### 2.2 Which words are "contested"?

| word         |happs    |stddev    |
| -------------|---------|----------|
| fucking      |4.64     |2.9260    |
| fuckin       |3.86     |2.7405    |
| fucked       |3.56     |2.7117    |
| pussy        |4.80     |2.6650    |
| whiskey      |5.72     |2.6422    |
| slut         |3.57     |2.6300    |
| cigarettes   |3.31     |2.5997    |
| fuck         |4.14     |2.5794    |
| mortality    |4.38     |2.5546    |
| cigarette    |3.09     |2.5163    |
| motherfuckers|2.51     |2.4675    |
| churches     |5.70     |2.4599    |
| motherfucking|2.64     |2.4558    |
| capitalism   |5.16     |2.4524    |
| porn         |4.18     |2.4302    |

Of the 15 most contested words, that is, words with the highest standard deviation across all corpuses, 87%  fall below the general mean and median happiness score, with a little over 50% falling into the category of profanity and the rest being divided between 'guilty pleasures' (e.h. "whiskey", "cigarettes" or "porn") or "polarizing subjects" (e.g. "capitalism" or "churches").

Interestingly, analyzing the lists of most contested words per corpus shows the highest overlap between the general dataset, Twitter and Lyrics, mostly across the category of profanity; meanwhile Google Books and NYT have the highest overlap on polarizing subjects, particularly political and religious ones.

On a larger scale, comparing scatter plots of standard deviation per corpus, shows a persistant and expected fan-shaped pattern, consistently clustering about the mean with a tendency towards lower standard deviation in that area. Furthermore, it reveals that Music Lyrics not only overlap the most in terms top contested words with the combined dataset but may in fact be the main contributor.

### 2.3 Corpus Comparison

  
### 3.1 “exhibit” of words

####  Very positive
Words “laughter”, “happiness”, “love”, “happy”, “ laughed” are rated very positive. These words don’t have any ambiguity, therefor no conflict in meaning interpretation.

#### Very negative
Words “terrorist”, “suicide”, “rape”, “terrorism”, “murder” were rated as very negative. These words don’t have any ambiguity either and the rating reflects that.

#### Highly contested
“Whiskey” can be associated with a positive connotation, such as a party or drinking with friends, but it can also be associated with alcoholism or health risks. A community that follows religious restrictions on alcohol can interpret this word negatively. Words like “pussy”, “fucked” , ‘fucking”, “fuckin’ can be interpreted as slurs or words relating to intercourse, which can have both positive or negative interpretations, hence the conflicting ratings.

#### Weird/culturally loaded
The following words are context sensitive, and since they were rated as stand-alone words, they may have been interpteted diffenently.

“Proportions” and “lift” are words with several meanings. Lift can refer to weightlifting or picking things up, an uplifted mood, a facelift, or shoplifting. "Proportions" is a term used in mathematical and health domains. A more common/everyday use can be “body proportions”. The rating for these words is based on what the annotators associated them with which is more subjective.

“Stevens” being a name (last name or place name) is challenging to accurately interpret without surrounding text or other clarifications of what it refferes to.

“2nd” can be interpreted as second place, which can be either positiv e(as in its second-best) or negative (that its not the best one).

“Orleans” — refers to New Orleans. The scores are likely based on personal associations with said location. New Orleans is famous for its jazz music. People who like the genre will likely rate the word positively. Natural disasters, on the other hand, are a frequent occurrence in New Orleans, which can contribute to a negative association and a score.

Other observations:

1. Words rated as “very positive” show low rating variance.
2. Highly contested words show the highest standard deviation across all categories; however, some words score close to neutral, like "fucking" (4.64 happiness score) and "pussy" (4.8 happiness score). These words are rather neutural than contested.
3. “Weird / culturally loaded” words cluster around the middle — the deviation from 5 (the midpoint) is minimal. This suggests the actual usage of these words is not prominent, but rather the score is affected by context variability.
4. “Very negative words” have the lowest rate of deviation.


### 4.1 Reconstructing the pipeline (data provenance)

1.Word Selection: Researchers complied a list of 10,000 frequently used English words from various sources.

2.Happiness Ratings: Each word was shown to 50 different workers on Amazon Mechanical Turk, who rated how happy the word made them feel on a scale of 1  (sad) to 9 (happy).

3.Score calculation: For each word they calculated average hapiness score (mean of 50 ratings) and standard deviation (how much ratings varied).

4.Corpus Frequency Analysis: Words were ranked by how often they appear in four different collection which includes twitter posts, google books, New York Times articles and song lyrics.

All data was combined into a single tab-delimited filed named Data set S1, referenced as labMT 1.0. 

### 4.2 Consequences & Limitations

1.Static Word Meanings - The instrument does not account for words with multiple meanings (polysemi). While the researchers argue that such errror is overrided by the massive dataset, it remains a limitation for fine-grained analysis. 

2.Counting different forms of the same word - The study avoided "stemming" meaning words, so it treated several word forms as unique entries with their own scores. This makes it easier to see distinct emotional nuances provided by tense and context. For example, the researchers found that "captured" (3.22) has a significantly different score than "capture". However, this makes it harder to aggregate the total frequency of an underlying concept as the data for a single idea is split across many different word forms. 

3.Omitting rare or specialized words displaying emotion - Instead of selecting words based on their emotional meaning, the researchers merged the top 5000 most frequent words from four disparate sources: Twitter, Google Books, music lyrics, and the New York Times. This makes it easier to achieve high "coverage" of a text, ensuring the instrument has data for a large percentage of the words actually being used in common language. However, it makes it harder to see the emotional impact of rare or specialized words that may carry heavy sentiment but do not appear frequently enough to make the top 5,000 list

4.Absence of Context and Structure - Text is treated a simple collection of words, calculating happiness based on individual word frequencies while ignoring sentence structure or word order. This makes the instrument transparent, fast, and highly robust when dealing with "web-scale" data like billions of tweets, where structural complexity might be computationally prohibitiveConversely, it cannot account for word order or negated sentiments (e.g., "not happy"), which effectively omits a significant portion of a text's actual content. It makes it hard to also recognize meaning in small texts (like single sentences) where irony, sarcasm, or negation (e.g., "not happy") would completely change the sentiment but are missed by a word-by-word average

5.Contamination from accounts with disputed authenticity - The dataset treats all accounts equally, meaning the emotional signal is a blend of accounts belonging to individuals, news organisations, companies and automated bots. This makes it difficult to distinguish genuine human sentiment from corporate broadcasting. The dataset is also vulnerable to entities that intentionally alter expressions online to misinform and manipulate. 

### 4.3 Instrument note

4.3.1 What can this data set be trusted to measure well?
This hedonometor can only measure exhibited behavior. It can quantify exhibited emotional tone as perceived by a generic user of Twitter. It is unable to reflect accurately actual internal emotional states or private beliefs of individuals or populations included.

4.3.2 What claims can NOT be made based on this data set?
While the patterns observed in the data might suggest universal human behaviors, those cannot be be statistically generalized to the broader population. Twitter user accounts are a non-representative population.

4.3.3. Possible improvements

The dataset can be updated to include modern slang, hashtags, and cultural references that have evolved since its creation. 

Instead of single words, the instrument could include common short phrases. This would make handling negation possible ("not happy") and could include indicative short phrases ("child abuse", "sex scandal") to provide more accurate sentiment readings. 

Another significant improvement would be distinguishing between human users and automated bots or news organizations, which currently mix individual emotional signal with corporate or automated messaging.

Future research could leverage more detailed metadata to explore geographic variations/

### Tools Used
For this assignment there were various tools used to help with writing code in parts that were difficult. Those tools include recommended UVA AI Chat and ChatGPT free version. Notebook LLM was used to better dissect the assigned research paper and understand statistical concepts from it.
