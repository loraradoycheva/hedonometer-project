import pandas as pd
from collections import Counter



count_2015 = pd.read_csv("data/cache/2015/word_counter_2015.csv")
count_2015_dict = dict(zip(count_2015["word"], count_2015["count"]))

count_2016 = pd.read_csv("data/cache/2016/word_counter_2016.csv")
count_2016_dict = dict(zip(count_2016["word"], count_2016["count"]))

count_2017 = pd.read_csv("data/cache/2017/word_counter_2017.csv")
count_2017_dict = dict(zip(count_2017["word"], count_2017["count"]))

count_2018 = pd.read_csv("data/cache/2018/word_counter_2018.csv")
count_2018_dict = dict(zip(count_2018["word"], count_2018["count"]))

count_2019 = pd.read_csv("data/cache/2019/word_counter_2019.csv")
count_2019_dict = dict(zip(count_2019["word"], count_2019["count"]))

count_2020 = pd.read_csv("data/cache/2020/word_counter_2020.csv")
count_2020_dict = dict(zip(count_2020["word"], count_2020["count"]))

count_2021 = pd.read_csv("data/cache/2021/word_counter_2021.csv")
count_2021_dict = dict(zip(count_2021["word"], count_2021["count"]))

count_2022 = pd.read_csv("data/cache/2022/word_counter_2022.csv")
count_2022_dict = dict(zip(count_2022["word"], count_2022["count"]))

count_2023 = pd.read_csv("data/cache/2023/word_counter_2023.csv")
count_2023_dict = dict(zip(count_2023["word"], count_2023["count"]))

count_2024 = pd.read_csv("data/cache/2024/word_counter_2024.csv")
count_2024_dict = dict(zip(count_2024["word"], count_2024["count"]))

count_2025 = pd.read_csv("data/cache/2025/word_counter_2025.csv")
count_2025_dict = dict(zip(count_2025["word"], count_2025["count"]))

df_all = pd.read_csv('data/cache/word_counter_all.csv')


def add_2015_count(text):
    words = text.lower().split()
    new_count = [count_2015_dict[w] for w in words if w in count_2015_dict]
    return new_count

def add_2016_count(text):
    words = text.lower().split()
    new_count = [count_2016_dict[w] for w in words if w in count_2016_dict]
    return new_count

def add_2017_count(text):
    words = text.lower().split()
    new_count = [count_2017_dict[w] for w in words if w in count_2017_dict]
    return new_count

def add_2018_count(text):
    words = text.lower().split()
    new_count = [count_2018_dict[w] for w in words if w in count_2018_dict]
    return new_count

def add_2019_count(text):
    words = text.lower().split()
    new_count = [count_2019_dict[w] for w in words if w in count_2019_dict]
    return new_count

def add_2020_count(text):
    words = text.lower().split()
    new_count = [count_2020_dict[w] for w in words if w in count_2020_dict]
    return new_count

def add_2021_count(text):
    words = text.lower().split()
    new_count = [count_2021_dict[w] for w in words if w in count_2021_dict]
    return new_count

def add_2022_count(text):
    words = text.lower().split()
    new_count = [count_2022_dict[w] for w in words if w in count_2022_dict]
    return new_count

def add_2023_count(text):
    words = text.lower().split()
    new_count = [count_2023_dict[w] for w in words if w in count_2023_dict]
    return new_count

def add_2024_count(text):
    words = text.lower().split()
    new_count = [count_2024_dict[w] for w in words if w in count_2024_dict]
    return new_count

def add_2025_count(text):
    words = text.lower().split()
    new_count = [count_2025_dict[w] for w in words if w in count_2025_dict]
    return new_count


#for all
df_all["2015"] = df_all["word"].apply(add_2015_count)
df_all['2015'] = [''.join(map(str, l)) for l in df_all['2015']]

df_all["2016"] = df_all["word"].apply(add_2016_count)
df_all['2016'] = [''.join(map(str, l)) for l in df_all['2016']]

df_all["2017"] = df_all["word"].apply(add_2017_count)
df_all['2017'] = [''.join(map(str, l)) for l in df_all['2017']]

df_all["2018"] = df_all["word"].apply(add_2018_count)
df_all['2018'] = [''.join(map(str, l)) for l in df_all['2018']]

df_all["2019"] = df_all["word"].apply(add_2019_count)
df_all['2019'] = [''.join(map(str, l)) for l in df_all['2019']]

df_all["2020"] = df_all["word"].apply(add_2020_count)
df_all['2020'] = [''.join(map(str, l)) for l in df_all['2020']]

df_all["2021"] = df_all["word"].apply(add_2021_count)
df_all['2021'] = [''.join(map(str, l)) for l in df_all['2021']]

df_all["2022"] = df_all["word"].apply(add_2022_count)
df_all['2022'] = [''.join(map(str, l)) for l in df_all['2022']]

df_all["2023"] = df_all["word"].apply(add_2023_count)
df_all['2023'] = [''.join(map(str, l)) for l in df_all['2023']]

df_all["2024"] = df_all["word"].apply(add_2024_count)
df_all['2024'] = [''.join(map(str, l)) for l in df_all['2024']]

df_all["2025"] = df_all["word"].apply(add_2025_count)
df_all['2025'] = [''.join(map(str, l)) for l in df_all['2025']]



df_all = df_all.replace('', pd.NA)


df_all['2015'] = df_all['2015'].fillna(-1).astype(int)
df_all['2016'] = df_all['2016'].fillna(-1).astype(int)
df_all['2017'] = df_all['2017'].fillna(-1).astype(int)
df_all['2018'] = df_all['2018'].fillna(-1).astype(int)
df_all['2019'] = df_all['2019'].fillna(-1).astype(int)
df_all['2020'] = df_all['2020'].fillna(-1).astype(int)
df_all['2021'] = df_all['2021'].fillna(-1).astype(int)
df_all['2022'] = df_all['2022'].fillna(-1).astype(int)
df_all['2023'] = df_all['2023'].fillna(-1).astype(int)
df_all['2024'] = df_all['2024'].fillna(-1).astype(int)
df_all['2025'] = df_all['2025'].fillna(-1).astype(int)


df_all = df_all.replace(-1, pd.NA)


print(df_all.dtypes)
print(df_all.isnull().sum())

#df_all.to_csv('data/cache/data_all_combined.csv', index=False)


#for 2015-2019
df_2015_2019 = df_all.drop(['2020', '2021', '2022', '2023', '2024', '2025'], axis=1)

print(df_2015_2019.dtypes)
print(df_2015_2019.isnull().sum())

#df_2015_2019.to_csv('data/cache/data_2015_2019_combined.csv', index=False)


#for 2020-2025
df_2020_2025 = df_all.drop(['2015', '2016', '2017', '2018', '2019'], axis=1)

print(df_2020_2025.dtypes)
print(df_2020_2025.isnull().sum())

#df_2020_2025.to_csv('data/cache/data_2020_2025_combined.csv', index=False)