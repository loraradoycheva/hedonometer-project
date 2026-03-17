import pandas as pd

#load the dataset
df = pd.read_csv(
    "data/labMT1.txt",  #sep="\t" means the file is tab-separated
    sep="\t", 
    header=0  #this makes first row as names of the columns, i believe we skipped other metadata        
)
#in this table we focus on happs and stddev in the data 
df["happs"] = pd.to_numeric(df["happs"], errors="coerce")
df["stddev"] = pd.to_numeric(df["stddev"], errors="coerce")
#coerce turns weird stuff like -- into NaN

#for very positive words we take from most happy to least happy ones
very_positive = (
    df.sort_values("happs", ascending=False) #for positive words its going down from best to worst
      .head(5)[["word", "happs", "stddev"]]
)
#the same thing for negative, from bottom to the top
very_negative = (
    df.sort_values("happs", ascending=True)
      .head(5)[["word", "happs", "stddev"]]
)
#contested words are the ones with high standard deviation 
highly_contested = (
    df.sort_values("stddev", ascending=False)
      .head(5)[["word", "happs", "stddev"]]
)
#for weird words i decided to go with the ones in the middle instead of choosing
weird_words = (
    df[
        (df["happs"] > 4.5) &
        (df["happs"] < 6)
    ]
    .sample(5)[["word", "happs", "stddev"]]
)
#and now labels for each word in the exhibit that can be used in the readme 
very_positive["category"] = "Very positive"
very_negative["category"] = "Very negative"
highly_contested["category"] = "Highly contested"
weird_words["category"] = "Weird / culturally loaded"
exhibit = pd.concat( #this makes the tables merge into one big
    [very_positive, very_negative, highly_contested, weird_words]
)
print("\nWORD EXHIBIT (20 WORDS):\n") #this prints the table in terminal 
print(exhibit)
#should work, the only problem is that it prints first word in the table as number 0, which i do not know how to change at this point 

from tabulate import tabulate #import the tabulate function(it is used for converting tables into markdown format table)

exhibit = exhibit.reset_index(drop=True)  # cleans the numbering: the Dataframe intex and rows are numbered 0-19. drop=True stops old indexes from being added again

markdown_table = tabulate(exhibit, headers="keys", tablefmt="github", showindex=False)
# convert the pandas DataFrame into a Markdown format table, assigns DataFrame column names as table headers, formats table into a GitHub-style Markdown and prevents row numbers (0,1,2...) from appearing

with open("word_exhibit.md", "w") as f: # creates or opens a file "word_exhibit.md" in writing mode. if the file a;ready exisst sa rnew random sample is generatred and the file is overwritten
    f.write(markdown_table) #writes the markdown table into the file

print("\nMarkdown table saved to 'word_exhibit.md'") # prints conformation message in terminal