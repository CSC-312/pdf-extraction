# %%
import sys
import pandas as pd
from pathlib import Path

# Add the project root to the Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from utils.logger import get_logger

logger = get_logger()

# %%
df_uwc = pd.read_excel("data/all-data.xlsx", sheet_name="uwc.ac.za with pdfs")
df_subdomains = pd.read_excel("data/all-data.xlsx", sheet_name="subdomains")
df_youtube = pd.read_excel("data/all-data.xlsx", sheet_name="youtube")
df_faq = pd.read_excel("data/all-data.xlsx", sheet_name="faq")
df_degrees = pd.read_excel("data/all-data.xlsx", sheet_name="degrees")
df_modules = pd.read_excel("data/all-data.xlsx", sheet_name="modules")


logger.info(
    f"{df_uwc.__len__() + df_degrees.__len__() + df_modules.__len__()} total PDFs before cleaning."
)

# %%
df_uwc = df_uwc[df_uwc["url"].str.endswith("pdf")]
df_uwc = df_uwc[["url"]].copy()
df_uwc.drop_duplicates(inplace=True)
df_uwc = df_uwc[
    ~(
        df_uwc["url"].str.contains("conference", case=False, na=False)
        | df_uwc["url"].str.contains("src", case=False, na=False)
        | df_uwc["url"].str.contains("chapter", case=False, na=False)
        | df_uwc["url"].str.contains("filesusr", case=False, na=False)
        | df_uwc["url"].str.contains("meltwaterafrica", case=False, na=False)
        | df_uwc["url"].str.contains("speech", case=False, na=False)
        | df_uwc["url"].str.contains("pptx", case=False, na=False)
        | df_uwc["url"].str.contains("map", case=False, na=False)
        | df_uwc["url"].str.contains("dammert", case=False, na=False)
        | df_uwc["url"].str.contains(".com", case=False, na=False)
        | df_uwc["url"].str.contains(".co.za", case=False, na=False)
        | df_uwc["url"].str.contains(".org", case=False, na=False)
        | df_uwc["url"].str.contains("policy", case=False, na=False)
        | df_uwc["url"].str.contains(
            "365|1994|1995|1996|1997|1998|1999|2000|2001|2002|2003|2004|2005|2006|2007|2008|2009|2010|2011|2012|2013|2014|2015|2016|2017|2018|2019|2020|2021|2022|2023|2024",
            regex=True,
            na=False,
        )
    )
]

logger.info("Cleaning data...")
# %%
df_degrees.drop_duplicates(inplace=True)

# %%
df_modules = df_modules[["url"]].copy()
df_modules.drop_duplicates(inplace=True)

# %%
df = pd.concat([df_uwc, df_degrees, df_modules])
# %%
logger.info(f"{df.__len__()} total PDFS in the dataframe after cleaning.")

df.to_csv("data/pdfs.csv", index=False)
