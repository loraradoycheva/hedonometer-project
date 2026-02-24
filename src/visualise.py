import pandas as pd
import matplotlib.pyplot as plt
#tell Python which libraries to use

df = pd.read_csv('data/labMT1.txt', sep='\t', comment='#')
df = df.replace('--', pd.NA)
numeric_cols = df.columns.drop('word')
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
# load the file, replace missing values, convert numbers.
plt.figure(figsize=(10, 6))
#Creates a blank canvas for your graph. figsize=(10, 6) sets the width and height in inches.
plt.hist(df['happs'], bins=30)
#plt.hist draws the histogram df happs means use the happs column. bins=30 means divide the scores into 30 groups. 
plt.title('Distribution of Happiness Scores (labMT 1.0)')
plt.xlabel('Happiness Score (1-9)')
plt.ylabel('Number of Words')
#These add the title and axis labels. Without these the graph has no explanation — the assignment specifically requires them.
plt.savefig('figures/histogram_happs.png')
#Saves the graph as an image file in your figures
plt.show()  
#Opens the graph
print(df['happs'].mean())
#average of all scores
print(df['happs'].median())
#he middle value when all scores are sorted
print(df['happs'].std())
#standard deviation, how spread out the scores are
print(df['happs'].quantile(0.05))
#the value below which 5% of words fall
print(df['happs'].quantile(0.95))
#the value below which 95% of words fall
plt.figure(figsize=(10, 6))
plt.scatter(df['happs'], df['stddev'], alpha=0.3)
#scatter makes scatterploy, every word a dot. happs = x,sttdev = y. alpha=0.3 makes each dot 30% opaque, so where many dots overlap it looks darker
plt.title('Happiness Score vs Standard Deviation')
plt.xlabel('Happiness Score (1-9)')
plt.ylabel('Standard Deviation')
#standard deviation measures how spread out the ratings are from the average
plt.savefig('figures/scatter_happs_stddev.png')
plt.show()
print(df.nlargest(15, 'stddev')[['word', 'happs', 'stddev']])
missing_r1 = set(df[df['rank.1'].isna()]['word'])
missing_r2 = set(df[df['rank.2'].isna()]['word'])
print(len(missing_r1 & missing_r2))
print('Twitter:', df['rank.1'].notna().sum())
print('Google Books:', df['rank.2'].notna().sum())
print('NYT:', df['rank.3'].notna().sum())
print('Lyrics:', df['rank.4'].notna().sum())
r1 = set(df[df['rank.1'].notna()]['word'])
r2 = set(df[df['rank.2'].notna()]['word'])
r3 = set(df[df['rank.3'].notna()]['word'])
r4 = set(df[df['rank.4'].notna()]['word'])

print('Twitter & Google Books:', len(r1 & r2))
print('Twitter & NYT:', len(r1 & r3))
print('Twitter & Lyrics:', len(r1 & r4))
print('Google Books & NYT:', len(r2 & r3))
print('Google Books & Lyrics:', len(r2 & r4))
print('NYT & Lyrics:', len(r3 & r4))
print('All four:', len(r1 & r2 & r3 & r4))

labels = ['Twitter &\nGoogle Books', 'Twitter &\nNYT', 'Twitter &\nLyrics', 
          'Google Books &\nNYT', 'Google Books &\nLyrics', 'NYT &\nLyrics', 'All four']
overlaps = [2696, 2881, 3127, 3414, 2368, 2241, 1816]

plt.figure(figsize=(10, 6))
plt.bar(labels, overlaps)
plt.title('Word Overlap Between Corpora')
plt.ylabel('Number of Words in Common')
plt.savefig('figures/corpus_comparison.png')
plt.show()

print('total rows:', len(df))
print('rank.1 missing:', df['rank.1'].isna().sum())
print('rank.1 present:', df['rank.1'].notna().sum())
print('missing + present:', df['rank.1'].isna().sum() + df['rank.1'].notna().sum())