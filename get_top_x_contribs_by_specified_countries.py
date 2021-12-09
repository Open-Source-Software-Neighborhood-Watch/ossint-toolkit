"""Create table of contributor count for specified countries by package

Input: csv with fields of (software_name, username, location, country)
Ouput: csv with fields of (package, us, china, russia, other, none) with
       contributor counts

This analysis was created as part of the "choosing sides" research project
within the larger open code project.

Programmer: John Speed Meyers
Project: Choosing Sides
Organization: IQT Labs, IQT
"""
import time

import pandas as pd

# number of top contributors to perform filtering
TOP_CONTRIB_NUM = 100

INPUT_FILE = "../processed_data/top_approx_70_unique_npm_links_contribs_mar_8_2021.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILE = (
    "../processed_data/npm_top_"
    + str(TOP_CONTRIB_NUM)
    + "_pkgs_by_country_"
    + DATETIME_STAMP
    + ".csv"
)


df = pd.read_csv(INPUT_FILE)

df = df.groupby("software_name").head(TOP_CONTRIB_NUM)

# if country is not us, china, russia, or none, set to other
df.loc[
    ~df["country"].isin(["United States", "China", "Russia", "None"]), "country"
] = "Other"

# cross tabulation of package by country
res = pd.crosstab(df["software_name"], df["country"])

# uncomment to show all rows when printing res
pd.set_option('display.max_rows', None)

# reorder columns
res = res[["United States", "China", "Russia", "Other", "None"]]

print(res)

# export results
res.to_csv(OUTPUT_FILE, index=False)
