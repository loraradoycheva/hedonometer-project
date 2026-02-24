import pandas as pd   
#name pandas pd   
df = pd.read_csv('data/labMT1.txt', sep='\t', comment='#') 
#df=storageplace for table. Use panda to read file and turn into table.
#Columns separated by tab, ignore the beginning with hashtags. 
print(df.shape)
#show the dataframe. Shape = property that tells size. Together: show me size of my table
print(df.head())
#show me first five rows of table (head). 
df = df.replace('--', pd.NA) #find every -- in the table and replace it with a proper empty value
print(df.isnull().sum()) #checks every cell: "is this empty?" Returns True or False for each cel
#out of all the words, 5192 didn't appear in top 5000 rank for all four categories
numeric_cols = df.columns.drop('word')
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')
#go through every column, try to convert it to numbers. Skip the words column.
print(df.dtypes)
print(df.duplicated().sum()) 
#checks for duplicates .sum() then counts all the Trues
print(df.sample(5))
print(df.nlargest(10, 'happs'))
print(df.nsmallest(10, 'happs'))
#Prints random, highest and lowest values 

