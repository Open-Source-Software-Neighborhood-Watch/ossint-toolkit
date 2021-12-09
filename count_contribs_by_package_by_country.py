"""Create table of contributor count for specified countries by package

Input: csv with fields of (software_name, username, location, country)
Ouput: csv with fields of (software_name, china, russia) with contributor counts

This analysis was originally created as part of the "choosing sides"
research project within the larger open code project.

Programmer: John Speed Meyers
Project: Julia Ecosystem Analysis
Organization: IQT Labs, IQT
"""
import time

import pandas as pd

# number of top contributors to perform filtering
TOP_CONTRIB_NUM = 10

INPUT_FILE = "../processed_data/julia_results_combined_gitgeo-20211108-101909.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILE = (
    "../processed_data/julia_top_"
    + str(TOP_CONTRIB_NUM)
    + "_pkgs_by_country_"
    + DATETIME_STAMP
    + ".csv"
)


df = pd.read_csv(INPUT_FILE)

df = df.groupby("software_name").head(TOP_CONTRIB_NUM)

# cross tabulation of package by country
res = pd.crosstab(df["software_name"], df["country"])

# uncomment to show all rows when printing res
# pd.set_option('display.max_rows', None)
# print(res)

# reorder columns
res = res[["China", "Russia"]]

# export results
res.to_csv(OUTPUT_FILE)
