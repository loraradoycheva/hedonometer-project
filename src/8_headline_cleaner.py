import pandas as pd



hedonometer = pd.read_csv("data/labMT1.txt", sep="\t", comment="#")
hedonometer = hedonometer.replace("--", pd.NA)
hedonometer["happs"] = pd.to_numeric(hedonometer["happs"], errors="coerce")
happs_dict = dict(zip(hedonometer["word"], hedonometer["happs"]))

df_all = pd.read_csv('data/cache/data_all.csv')

df_all_v1 = df_all



def score_headline(text):
    words = text.lower().split()
    scores = [happs_dict[w] for w in words if w in happs_dict]
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)



df_all_v1["happs_score"] = df_all_v1["headline"].apply(score_headline)
df_all_v1['pub_date'] = pd.to_datetime(df_all_v1['pub_date']).dt.date



df_all_v2 = df_all_v1.drop(['abstract', 'document_type', '_id', 'keywords', 'news_desk', 'print_page', 'print_section', 'section_name', 'snippet',
                           'source', 'subsection_name', 'type_of_material', 'uri', 'web_url', 'word_count', 'byline.original', 'headline.main',
                           'headline.kicker', 'headline.print_headline', 'multimedia.caption', 'multimedia.credit', 'multimedia.default.url',
                           'multimedia.default.height', 'multimedia.default.width', 'multimedia.thumbnail.url', 'multimedia.thumbnail.height',
                           'multimedia.thumbnail.width', 'text'], axis=1)


df_all_v2.to_csv('data/cache/headlines_clean_scored_all.csv', index=False)