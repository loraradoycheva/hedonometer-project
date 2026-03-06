import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

df = pd.read_csv('data/labMT1.txt', sep='\t', header=0, comment='#')  
df = df.replace('--', pd.NA)
numeric_cols = df.columns.drop('word')
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')


df_1 = df.rename(columns={'rank.1':'twitter', 'rank.2':'google', 'rank.3':'nyt', 'rank.4':'lyrics'})
#print(df_1.describe().drop(['count']).drop(['rank', 'stddev'], axis=1))

df_twitter = df_1.loc[:, :'twitter'].dropna()
#print(df_twitter)

df_google = df_1[['word', 'rank', 'happs', 'stddev', 'google']].dropna()
#print(df_google)

df_nyt = df_1[['word', 'rank', 'happs', 'stddev', 'nyt']].dropna()
#print(df_nyt)

df_lyrics = df_1[['word', 'rank', 'happs', 'stddev', 'lyrics']].dropna()
#print(df_lyrics)




fig, ax = plt.subplots(nrows=1, ncols=4, squeeze=False, sharey=True, figsize=(13,18))
sns.boxplot(data=df_twitter, y='happs', showmeans=True, meanline=True, flierprops={"marker": "x"}, boxprops={"facecolor": (.3, .5, .7, .5)}, medianprops={"color": "r", "linewidth": 2}, ax=ax[0, 0], width=.5)
ax[0,0].set_ylabel('Distribution of Happiness Scores', fontsize=13)
ax[0,0].set_xlabel('Twitter', fontsize=13)
sns.boxplot(data=df_google, y='happs', showmeans=True, meanline=True, flierprops={"marker": "x"}, boxprops={"facecolor": (.3, .5, .7, .5)}, medianprops={"color": "r", "linewidth": 2}, ax=ax[0, 1], width=.5)
ax[0,1].set_xlabel('Google Books', fontsize=13)
sns.boxplot(data=df_nyt, y='happs', showmeans=True, meanline=True, flierprops={"marker": "x"}, boxprops={"facecolor": (.3, .5, .7, .5)}, medianprops={"color": "r", "linewidth": 2}, ax=ax[0, 2], width=.5)
ax[0,2].set_xlabel('NYT', fontsize=13)
sns.boxplot(data=df_lyrics, y='happs', showmeans=True, meanline=True, flierprops={"marker": "x"}, boxprops={"facecolor": (.3, .5, .7, .5)}, medianprops={"color": "r", "linewidth": 2}, ax=ax[0, 3], width=.5)
ax[0,3].set_xlabel('Music Lyrics', fontsize=13)

plt.savefig('figures/boxplots_compare.png')





fig, ax = plt.subplots(nrows=2, ncols=2, squeeze=False, sharey=True, sharex=True, figsize=(20,20))
sns.scatterplot(data=df_twitter, x='happs', y='stddev', edgecolor="None", alpha=0.6, s=10, ax=ax[0, 0])
ax[0,0].set_ylabel('Standard Deviation', fontsize=13)
ax[0,0].set_title('Twitter', fontsize=18)
sns.scatterplot(data=df_google, x='happs', y='stddev', edgecolor="None", alpha=0.6, s=10, ax=ax[0, 1])
ax[0,1].set_title('Google Books', fontsize=18)
sns.scatterplot(data=df_nyt, x='happs', y='stddev', edgecolor="None", alpha=0.6, s=10, ax=ax[1, 0])
ax[1,0].set_ylabel('Standard Deviation', fontsize=13)
ax[1,0].set_xlabel('Happiness Score (1-9)', fontsize=13)
ax[1,0].set_title('NYT', fontsize=18)
sns.scatterplot(data=df_lyrics, x='happs', y='stddev', edgecolor="None", alpha=0.6, s=10, ax=ax[1, 1])
ax[1,1].set_xlabel('Happiness Score (1-9)', fontsize=13)
ax[1,1].set_title('Music Lyrics', fontsize=18)

plt.savefig('figures/stddev_compare.png')





fig, ax = plt.subplots(nrows=2, ncols=2, squeeze=False, sharey=True, sharex=True, figsize=(10,10))
sns.histplot(data=df_twitter, x='happs', ax=ax[0, 0])
ax[0,0].set_ylabel('Word Count', fontsize=11)
ax[0,0].set_title('Distribution of Happiness Scores (Twitter)', fontsize=13)
sns.histplot(data=df_google, x='happs', ax=ax[0, 1])
ax[0,1].set_ylabel('Word Count', fontsize=11)
ax[0,1].set_title('Distribution of Happiness Scores (Google Books)', fontsize=13)
sns.histplot(data=df_nyt, x='happs', ax=ax[1, 0])
ax[1,0].set_ylabel('Word Count', fontsize=11)
ax[1,0].set_xlabel('Happiness Score (1-9)', fontsize=11)
ax[1,0].set_title('Distribution of Happiness Scores (NYT)', fontsize=13)
sns.histplot(data=df_lyrics, x='happs', ax=ax[1, 1])
ax[1,1].set_xlabel('Happiness Score (1-9)', fontsize=11)
ax[1,1].set_title('Distribution of Happiness Scores (Music Lyrics)', fontsize=13)

plt.savefig('figures/distr_compare.png')





fig, ax = plt.subplots(sharey=True, figsize=(10,10))
sns.kdeplot(data=df_twitter, x='happs', ax=ax, legend=True)
sns.kdeplot(data=df_google, x='happs', ax=ax, label='Google Books')
sns.kdeplot(data=df_nyt, x='happs', ax=ax, label='NYT')
sns.kdeplot(data=df_lyrics, x='happs', ax=ax, label='Song Lyrics')

fig.legend(['Twitter', 'Google Books', 'NYT', 'Music Lyrics'], loc='right', bbox_to_anchor=(0.35, 0.3, 0.5, 0.5))

plt.xlabel('Happiness Score (1-9)', fontsize=18)
plt.ylabel('Word Density', fontsize=16)
plt.title('Comparative Word Density', fontsize=20)

plt.savefig('figures/density_compare.png')
#plt.show()