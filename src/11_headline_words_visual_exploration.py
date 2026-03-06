import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("whitegrid")

df_2015_2019 = pd.read_csv('data/cache/data_2015_2019_combined.csv')
df_2020_2025 = pd.read_csv('data/cache/data_2020_2025_combined.csv')


#print('2015:', df_2015_2019['2015'].notna().sum())
#print('2016:', df_2015_2019['2016'].notna().sum())
#print('2017:', df_2015_2019['2017'].notna().sum())
#print('2018:', df_2015_2019['2018'].notna().sum())
#print('2019:', df_2015_2019['2019'].notna().sum())


r1 = set(df_2015_2019[df_2015_2019['2015'].notna()]['word'])
r2 = set(df_2015_2019[df_2015_2019['2016'].notna()]['word'])
r3 = set(df_2015_2019[df_2015_2019['2017'].notna()]['word'])
r4 = set(df_2015_2019[df_2015_2019['2018'].notna()]['word'])
r5 = set(df_2015_2019[df_2015_2019['2019'].notna()]['word'])

print('2015 & 2016:', len(r1 & r2))
print('2015 & 2017:', len(r1 & r3))
print('2015 & 2018:', len(r1 & r4))
print('2015 & 2019:', len(r1 & r5))
print('2016 & 2017:', len(r2 & r3))
print('2016 & 2018:', len(r2 & r4))
print('2016 & 2019:', len(r2 & r5))
print('2017 & 2018:', len(r3 & r4))
print('2017 & 2019:', len(r3 & r5))
print('2018 & 2019:', len(r4 & r5))
print('All years:', len(r1 & r2 & r3 & r4 & r5))


overlap_data = {'Years' : ['2015 &\n2016', '2015 &\n2017', '2015 &\n2018', '2015 &\n2019', '2016 &\n2017',
          '2016 &\n2018', '2016 &\n2019', '2017 &\n2018', '2017 &\n2019', '2018 &\n2019', 'All years'],
          'Number of Overlapping Words' : [261, 218, 205, 192, 194, 167, 161, 145, 144, 122, 52]}

fig, ax = plt.subplots()
sns.barplot(x='Years', y='Number of Overlapping Words', data=overlap_data, dodge=False)
ax.set_title('Word Overlap Between Years', fontsize = 15)
ax.set_xlabel("Grouped Years between 2015 and 2019", fontsize=11)
ax.set_ylabel("Number of Overlapping Words", fontsize=11)
ax.tick_params(axis='both', labelsize=8)

#plt.savefig('figures/2015_2019_word_overlaps_bar.png')



r6 = set(df_2020_2025[df_2020_2025['2020'].notna()]['word'])
r7 = set(df_2020_2025[df_2020_2025['2021'].notna()]['word'])
r8 = set(df_2020_2025[df_2020_2025['2022'].notna()]['word'])
r9 = set(df_2020_2025[df_2020_2025['2023'].notna()]['word'])
r10 = set(df_2020_2025[df_2020_2025['2024'].notna()]['word'])
r11 = set(df_2020_2025[df_2020_2025['2025'].notna()]['word'])

print('2020 & 2021:', len(r6 & r7))
print('2020 & 2022:', len(r6 & r8))
print('2020 & 2023:', len(r6 & r9))
print('2020 & 2024:', len(r6 & r10))
print('2020 & 2025:', len(r6 & r11))

print('2021 & 2022:', len(r7 & r8))
print('2021 & 2023:', len(r7 & r9))
print('2021 & 2024:', len(r7 & r10))
print('2021 & 2025:', len(r7 & r11))

print('2022 & 2023:', len(r8 & r9))
print('2022 & 2024:', len(r8 & r10))
print('2022 & 2025:', len(r8 & r11))

print('2023 & 2024:', len(r9 & r10))
print('2023 & 2025:', len(r9 & r11))

print('2024 & 2025:', len(r10 & r11))

print('All years:', len(r6 & r7 & r8 & r9 & r10 & r11))


overlap_data = {'Years' : ['2020 &\n2021', '2020 &\n2022', '2020 &\n2023', '2020 &\n2024', '2020 &\n2025', '2021 &\n2022',
          '2021 &\n2023', '2021 &\n2024', '2021 &\n2025', '2022 &\n2023', '2022 &\n2024', '2022 &\n2025', '2023 &\n2024', '2023 &\n2025', '2024 &\n2025', 'All years'],
          'Number of Overlapping Words' : [221, 198, 190, 149, 144, 246, 215, 174, 154, 247, 196, 153, 200, 169, 145, 43]}

fig, ax = plt.subplots()
sns.barplot(x='Years', y='Number of Overlapping Words', data=overlap_data, dodge=False)
ax.set_title('Word Overlap Between Years', fontsize = 15)
ax.set_xlabel("Grouped Years between 2020 and 2025", fontsize=11)
ax.set_ylabel("Number of Overlapping Words", fontsize=11)
ax.tick_params(axis='both', labelsize=7)

#plt.savefig('figures/2020_2025_word_overlaps_bar.png')

print('All years:', len(r1 & r2 & r3 & r4 & r5 & r6 & r7 & r8 & r9 & r10 & r11)) #the number is apparently 29




df_2015 = df_2015_2019.loc[:, :'2015'].dropna()
df_2016 = df_2015_2019[['word', 'count', 'happs_score', 'stddev', '2016']].dropna()
df_2017 = df_2015_2019[['word', 'count', 'happs_score', 'stddev', '2017']].dropna()
df_2018 = df_2015_2019[['word', 'count', 'happs_score', 'stddev', '2018']].dropna()
df_2019 = df_2015_2019[['word', 'count', 'happs_score', 'stddev', '2019']].dropna()


fig, ax = plt.subplots(nrows=3, ncols=2, squeeze=False, sharey=False, sharex=False, figsize=(10,10))
sns.histplot(data=df_2015, x='happs_score', ax=ax[0, 0], color='tab:blue')
ax[0,0].set_ylabel('Word Count', fontsize=11)
ax[0,0].set_xlabel(' ')
sns.histplot(data=df_2016, x='happs_score', ax=ax[0, 1], color='tab:orange')
ax[0,1].set_ylabel('Word Count', fontsize=11)
ax[0,1].set_xlabel(' ')
sns.histplot(data=df_2017, x='happs_score', ax=ax[1, 0], color='tab:red')
ax[1,0].set_ylabel('Word Count', fontsize=11)
ax[1,0].set_xlabel(' ')
sns.histplot(data=df_2018, x='happs_score', ax=ax[1, 1], color='tab:green')
ax[1,1].set_ylabel('Word Count', fontsize=11)
ax[1,1].set_xlabel(' ')
sns.histplot(data=df_2019, x='happs_score', ax=ax[2, 0], color='tab:purple')
ax[2,0].set_ylabel('Word Count', fontsize=11)
ax[2,0].set_xlabel('Happiness Score (1-9)', fontsize=11)
sns.kdeplot(data=df_2015, x='happs_score', ax=ax[2,1], linewidth=0.5, color= 'blue', legend=True)
sns.kdeplot(data=df_2016, x='happs_score', ax=ax[2,1], label='2016', linewidth=0.5, color= 'orange')
sns.kdeplot(data=df_2017, x='happs_score', ax=ax[2,1], label='2017', linewidth=0.5, color= 'red')
sns.kdeplot(data=df_2018, x='happs_score', ax=ax[2,1], label='2018', linewidth=0.5, color= 'green' )
sns.kdeplot(data=df_2019, x='happs_score', ax=ax[2,1], label='2019', linewidth=0.5, color= 'purple')
ax[2,1].set_ylabel('Word Density', fontsize=11)
ax[2,1].set_xlabel('Happiness Score (1-9)', fontsize=11)

fig.legend(['2015', '2016', '2017', '2018', '2019'], loc='right', bbox_to_anchor=(0.9, 0.25))

#plt.savefig('figures/2015_2019_word_distr_and_ked_comparison.png')




df_2020 = df_2020_2025.loc[:, :'2020'].dropna()
df_2021 = df_2020_2025[['word', 'count', 'happs_score', 'stddev', '2021']].dropna()
df_2022 = df_2020_2025[['word', 'count', 'happs_score', 'stddev', '2022']].dropna()
df_2023 = df_2020_2025[['word', 'count', 'happs_score', 'stddev', '2023']].dropna()
df_2024 = df_2020_2025[['word', 'count', 'happs_score', 'stddev', '2024']].dropna()
df_2025 = df_2020_2025[['word', 'count', 'happs_score', 'stddev', '2025']].dropna()


fig, ax = plt.subplots(nrows=4, ncols=2, squeeze=False, sharey=False, sharex=False, figsize=(10,10))
sns.histplot(data=df_2020, x='happs_score', ax=ax[0, 0], color='tab:blue')
ax[0,0].set_ylabel('Word Count', fontsize=11)
ax[0,0].set_xlabel(' ')
sns.histplot(data=df_2021, x='happs_score', ax=ax[0, 1], color='tab:orange')
ax[0,1].set_ylabel('Word Count', fontsize=11)
ax[0,1].set_xlabel(' ')
sns.histplot(data=df_2022, x='happs_score', ax=ax[1, 0], color='tab:red')
ax[1,0].set_ylabel('Word Count', fontsize=11)
ax[1,0].set_xlabel(' ')
sns.histplot(data=df_2023, x='happs_score', ax=ax[1, 1], color='tab:green')
ax[1,1].set_ylabel('Word Count', fontsize=11)
ax[1,1].set_xlabel(' ')
sns.histplot(data=df_2024, x='happs_score', ax=ax[2, 0], color='tab:purple')
ax[2,0].set_ylabel('Word Count', fontsize=11)
ax[2,0].set_xlabel('Happiness Score (1-9)', fontsize=11)
sns.histplot(data=df_2025, x='happs_score', ax=ax[2, 1], color='tab:grey')
ax[2,1].set_ylabel('Word Count', fontsize=11)
ax[2,1].set_xlabel('Happiness Score (1-9)', fontsize=11)
sns.kdeplot(data=df_2020, x='happs_score', ax=ax[3,0], linewidth=0.5, color= 'blue', legend=True)
sns.kdeplot(data=df_2021, x='happs_score', ax=ax[3,0], label='2021', linewidth=0.5, color= 'orange')
sns.kdeplot(data=df_2022, x='happs_score', ax=ax[3,0], label='2022', linewidth=0.5, color= 'red')
sns.kdeplot(data=df_2023, x='happs_score', ax=ax[3,0], label='2023', linewidth=0.5, color= 'green' )
sns.kdeplot(data=df_2024, x='happs_score', ax=ax[3,0], label='2024', linewidth=0.5, color= 'purple')
sns.kdeplot(data=df_2025, x='happs_score', ax=ax[3,0], label='2025', linewidth=0.5, color= 'black')
ax[3,0].set_ylabel('Word Density', fontsize=11)
ax[3,0].set_xlabel('Happiness Score (1-9)', fontsize=11)
fig.delaxes(ax[3,1])

fig.legend(['2020', '2021', '2022', '2023', '2024', '2025'], loc='lower center', bbox_to_anchor=(0.55, 0.11))

#plt.savefig('figures/2020_2025_word_distr_and_ked_comparison.png')


fig, ax = plt.subplots(sharey=True, figsize=(10,10))
sns.kdeplot(data=df_2015, x='happs_score', ax=ax, linewidth=0.5, color= 'tab:blue', legend=True)
sns.kdeplot(data=df_2016, x='happs_score', ax=ax, label='2016', linewidth=0.8, color= 'tab:orange')
sns.kdeplot(data=df_2017, x='happs_score', ax=ax, label='2017', linewidth=0.8, color= 'tab:red')
sns.kdeplot(data=df_2018, x='happs_score', ax=ax, label='2018', linewidth=0.8, color= 'tab:green' )
sns.kdeplot(data=df_2019, x='happs_score', ax=ax, label='2019', linewidth=0.8, color= 'tab:purple')
sns.kdeplot(data=df_2020, x='happs_score', ax=ax, label='2020', linewidth=0.8, color= 'tab:brown')
sns.kdeplot(data=df_2021, x='happs_score', ax=ax, label='2021', linewidth=0.8, color= 'tab:pink')
sns.kdeplot(data=df_2022, x='happs_score', ax=ax, label='2022', linewidth=0.8, color= 'tab:grey')
sns.kdeplot(data=df_2023, x='happs_score', ax=ax, label='2023', linewidth=0.8, color= 'tab:olive' )
sns.kdeplot(data=df_2024, x='happs_score', ax=ax, label='2024', linewidth=0.8, color= 'tab:cyan')
sns.kdeplot(data=df_2025, x='happs_score', ax=ax, label='2025', linewidth=0.8, color= 'yellow')

plt.xlabel('Happiness Score (1-9)', fontsize=18)
plt.ylabel('Word Density', fontsize=16)
plt.title('Comparative Word Density 2015-2025', fontsize=20)

fig.legend(['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025'], loc='right', bbox_to_anchor=(0.35, 0.3, 0.5, 0.5))

#plt.savefig('figures/2015_2025_ked_comparison.png')



df_headlines_15_19 = pd.read_csv('data/cache/headlines_clean_scored_2015_2019.csv')
df_headlines_15_19 = df_headlines_15_19.sort_values('pub_date').reset_index(drop=True)

df_headlines_20_25 = pd.read_csv('data/cache/headlines_clean_scored_2020_2025.csv')
df_headlines_20_25 = df_headlines_20_25.sort_values('pub_date').reset_index(drop=True)

#print(df_headlines_15_19)

fig, ax = plt.subplots(figsize=(35,15))
chrono_plot= sns.scatterplot(data=df_headlines_15_19, x="pub_date", y="happs_score", ax=ax)
for ind, label in enumerate(chrono_plot.get_xticklabels()):
    if ind % 20 == 0:
        label.set_visible(True)
    else:
        label.set_visible(False)
ax.tick_params(axis='both', labelsize=16)
plt.xticks(rotation=45)
plt.xlabel('Date', fontsize=25)
plt.ylabel('Aggregate Happiness Score', fontsize=25)
plt.title('Happiness Score of NYT Article Headlines Over Time (2015-2019) ', fontsize=30)

#plt.savefig('figures/2015_2019_headline_timeline.png')



fig, ax = plt.subplots(figsize=(35,15))
chronological_plot= sns.scatterplot(data=df_headlines_20_25, x="pub_date", y="happs_score", ax=ax)
for ind, label in enumerate(chronological_plot.get_xticklabels()):
    if ind % 20 == 0:
        label.set_visible(True)
    else:
        label.set_visible(False)
ax.tick_params(axis='both', labelsize=16)
plt.xticks(rotation=45)
plt.xlabel('Date', fontsize=25)
plt.ylabel('Aggregate Happiness Score', fontsize=25)
plt.title('Happiness Score of NYT Article Headlines Over Time (2020-2025) ', fontsize=30)

plt.savefig('figures/2020_2025_headline_timeline.png')


#plt.show()
