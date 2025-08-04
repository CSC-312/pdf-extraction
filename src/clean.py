# %%
import pandas as pd

# %%
df = pd.read_csv("data/UWC Website and PDF Data - Data.csv")

# %%
print(f"{df.__len__()} URLS in the dataframe.")

# %%
df = df[df['url'].str.endswith("pdf")] 

# %%
print(f"{df.__len__()} PDFS in the dataframe.")

# %%
# Keep only rows that do NOT match any of the patterns
df = df[
    ~(
        df['url'].str.contains("conference", case=False, na=False)
        | df['url'].str.contains("src", case=False, na=False)
        | df['url'].str.contains("chapter", case=False, na=False)
        | df['url'].str.contains("filesusr", case=False, na=False)
        | df['url'].str.contains("meltwaterafrica", case=False, na=False)
        | df['url'].str.contains("speech", case=False, na=False)
        | df['url'].str.contains("pptx", case=False, na=False)
        | df['url'].str.contains("map", case=False, na=False)
        | df['url'].str.contains("dammert", case=False, na=False)
        | df['url'].str.contains(".com", case=False, na=False)
        | df['url'].str.contains(".co.za", case=False, na=False)
        | df['url'].str.contains(".org", case=False, na=False)
        | df['url'].str.contains("policy", case=False, na=False)
        | df['url'].str.contains(
            "365|1994|1995|1996|1997|1998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021|2022|2023|2024",
            regex=True,
            na=False
        )
    )
]
# %%
print(f"{df.__len__()} PDFS in the dataframe after filtering.")

# %%
df['url'].to_csv('data/pdfs.csv', index=False, header=False)