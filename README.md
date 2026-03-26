# New York Times Headlines under a Hedonometer: Measuring Happiness in News Repoerting from 2015 to 2025

# Data Dictionary
| VARIABLE | DESCRIPTION | TYPE | MISSING VALUES |
|----------|-------------|------|----------------|
| **word** | the English word being rated | text | No missing values |
| **rank** | overall frequency rank across all corpora | integer | No missing values |
| **happs** | average happiness score (scale 1–9) | float | No missing values |
| **stddev** | standard deviation of happiness ratings (how much raters disagreed) | float | No missing values |
| **rank.1** | frequency rank in Twitter | float | 5192 missing values (word not in top 5000) |
| **rank.2** | frequency rank in Google Books | float | 5192 missing values |
| **rank.3** | frequency rank in New York Times | float | 5192 missing values |
| **rank.4** | frequency rank in Music Lyrics | float | 5192 missing values |

A missing rank means the word did not appear in the top 5000 most frequent 
words in that corpus.

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

### Research question:
Have news reports gotten sadder or more emotionally charged from 2015 till 2025 and what might be reasons for it / what can that indicate about current world affairs? 

### ​​Data:

- NYT Article Search API

 We collected approximately 1000 NYT World section headlines per year from 2019 to 2025 using the Article Search API. Requests filtered by section.name:("World") with 'sort=relevance' and an empty query string. Results are cached in 'data/cache/' as JSON files and treated as read-only. Each JSON file contains full article metadata, including headline, abstract, keywords, publication date, byline, and word count. Our analysis uses only the 'headline.main' field.

- labMT Hedonometer

 The labMT lexicon contains approximately 10,000 words rated for happiness on a 1-9 scale by Mechanical Turk workers. A score of 1 is very negative, 5 is neutral, and 9 is very positive. It was constructed from four corpora: Twitter, Google Books, NYT, and song lyrics. 

The NYT data was scored using the labMT dataset.

We have selected a time period from 2015 to 2025, separating it into two periods: before and after the pandemic.

 The justification for this choice is that the covid pandemic has significantly impacted many processes in the world. The public discourse commonly regards the years following the pandemic as “worse” than the ones prior to it. With our research question, we aimed at getting empirical evidence on whether the discourse  actually got sadder/ more charged.
​

#### Why did we choose to scrape data this way?

We have conditioned the script to scrape data under the “world” section, meaning that it will pull global news.

In order to get a neutral dataset, we have scraped headlines containing typical report words “claim”, “discuss”, “report “, and “state”. Forms/variants of the words also counted as long as the root was the same. 

The first 3 showed up as verbs; “state” occasionally showed up as a noun(as in “Islamic state”). Generally getting headlines with these words allowed us to access the discourse in the news articles. 

We have tested including “say” and its derivatives, following the same logic as the other report words. This filter, however, gave flawed results as “say” is so prevalent in the headlines and body text, respectively, api pulls articles for only the last months of the year, as it filters by “best fit” and “relevance,” and those conditions get fulfilled with the most recent data, that being the end of the year.

