# Seminars 3 & 4 — Hedonometer (Project Folder)

This folder provides an **example project structure** (and an instructor/demo script) for the Seminars 3 & 4 group project using the **labMT 1.0** dataset (Data Set S1 from the Hedonometer paper).

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

### 1) Create a virtual environment

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
### 1.2) Data Dictionary
- `word` - the english word that is being rated
  type: text, no missing values
- `rank` - placement of the word in the dataset
  type: integer, no missing values
- `happs` -  happiness rating on a scale from 1-9
  type: float, no missing values
- `stddev` - the vatiation of ratings across different annotators
  type: float, no missing values
- `1rank` - frequency on twitter
  type: integer, values are missing
- `2rank` - frequency on google
  type: integer, values are missing
- `3rank` - frequency in NYT articles
  type: integer, values are missing
- `4rank` - frequency in lyrics
  type: integer, values are missing
  
### 3.1) “exhibit” of words

####  Very positive
Words “laughter”, “happiness”, “love”, “happy”, “ laughed” are rated very positive. These words don’t have any ambiguity, therefor no conflict in meaning interpretation.

#### Very negative
Words “terrorist”, “suicide”, “rape”, “terrorism”, “murder” were rated as very negative. These words also have one meaning and the rating reflects that.

#### Highly contested
“Whiskey” can be associated with a positive connotation, such as a party or drinking with friends, but it can also be associated with alcoholism or health risks. A community that follows religious restrictions on alcohol can interpret this word negatively. Words “pussy”, “fucked” , ‘fucking”, “fuckin’ can be interpreted as slurs or words relating to intercourse, which can have both positive or negative interpretations, hence the conflicting ratings.

#### Weird / culturally loaded
These words are context sensitive, and as they were rated as stand alone words, they may have been interpteted diffenenrly.

“Proportions” and “lift” are words with several meanings. Lift can refer to: weightlifting or picking things up, a lifted mood, a facelift, or shoplifting. Proportions are a term used in math, statistics, and health. A more common/everyday use can be “body proportions”. The rating for these words is based on what the annotator associated them with.

“Stevens” being a name(last name or place name) is challenging to accurately inbterpreted without surrounding text or other clarifications of what it refferes to.

“2nd” can be interpreted as second place, which can be either positive(as in its second-best) or negative(that its not the best one).

“Orleans” — refers to New Orleans. The scores are likely based on personal associations with said location. New Orleans is famous for its jazz music, so people who like that will likely rate the word positively. Natural disasters are a frequent occurrence in New Orleans, which can contribute to a negative association and a score, respectively.

Other observations:

1. Words rated as “very positive” show low rating variance.
2. Highly contested words show the highest standard deviation across all categories; however, some words score close to neutral, like fucking (4.64 happiness score) and pussy (4.8 happiness score). These words are rather neutural that contested.
3. “Weird / culturally loaded” words cluster around the middle — the deviation from 5(the midpoint) is minimal. This suggests that the actual polarity of these words is not prominent, but rather the score is affected by context variability.
4. “Very negative words” have the lowest rate of deviation.


4.1 Reconstruct the pipeline (data provenance)

1.Word Selection: Researchers complied a list of 10,000 frequently used English words from various sources.

2.Happiness Ratings: Each word was shown to 50 different workers on Amazon Mechanical Turk, who rated how happy the word made them feel on a scale of 1  (sad) to 9 (happy).

3.Score calculation: For each word they calculated average hapiness score (mean of 50 ratings) and standard deviation (how much ratings varied).

4.Corpus Frequency Analysis: Words were ranked by how often they appear in four different collection which includes twitter posts, google books, New York Times articles and song lyrics.

All data was combined into a single tab-delimited filed named Data set S1, referenced as labMT 1.0. 
