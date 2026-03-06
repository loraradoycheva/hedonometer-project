import pandas as pd
from collections import Counter
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS



hedonometer = pd.read_csv("data/labMT1.txt", sep="\t", comment="#")
hedonometer = hedonometer.replace("--", pd.NA)
hedonometer["happs"] = pd.to_numeric(hedonometer["happs"], errors="coerce")
happs_dict = dict(zip(hedonometer["word"], hedonometer["happs"]))
stddev_dict = dict(zip(hedonometer["word"], hedonometer["stddev"]))

df_2020 = pd.read_csv('data/cache/2020/data_2020.csv')

df_2020_v1 = df_2020



df_2020_v1['pub_date'] = pd.to_datetime(df_2020_v1['pub_date']).dt.date



df_2020_v2 = df_2020_v1.drop(['abstract', 'document_type', '_id', 'keywords', 'news_desk', 'print_page', 'print_section', 'pub_date', 'section_name', 'snippet',
                           'source', 'subsection_name', 'type_of_material', 'uri', 'web_url', 'word_count', 'byline.original', 'headline.main',
                           'headline.kicker', 'headline.print_headline', 'multimedia.caption', 'multimedia.credit', 'multimedia.default.url',
                           'multimedia.default.height', 'multimedia.default.width', 'multimedia.thumbnail.url', 'multimedia.thumbnail.height',
                           'multimedia.thumbnail.width', 'text'], axis=1)




df_2020_v2['headline'] = df_2020_v2['headline'].str.split(' ')
df_2020_v2['headline'].to_list()
df_2020_v3 = df_2020_v2.explode('headline')
df_2020_v3['headline'] = df_2020_v3['headline'].str.lower()




all_words = []
for headline in df_2020_v3['headline']:
    words = headline.lower().split()
    all_words.extend(words)

word_counts = Counter(all_words)

stop_words = set(ENGLISH_STOP_WORDS)

word_counts = {w: c for w, c in word_counts.items() 
               if w not in stop_words 
               and w in happs_dict  # only hedonometer words!
               and len(w) > 2}

#print(type(word_counts))

df_count_2020 = pd.DataFrame(word_counts.items(), columns=['word', 'count'])
df_count_2020.drop_duplicates()



def score_headline(text):
    words = text.lower().split()
    scores = [happs_dict[w] for w in words if w in happs_dict]
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)

def add_stddev(text):
    words = text.lower().split()
    deviations = [stddev_dict[w] for w in words if w in stddev_dict]
    return deviations

df_count_2020["happs_score"] = df_count_2020["word"].apply(score_headline)
df_count_2020["stddev"] = df_count_2020["word"].apply(add_stddev)
df_count_2020['stddev'] = [''.join(map(str, l)) for l in df_count_2020['stddev']]
df_count_2020['stddev'] = df_count_2020['stddev'].astype(float)

print(df_count_2020.dtypes)

df_count_2020.to_csv('data/cache/2020/word_counter_2020.csv', index=False)