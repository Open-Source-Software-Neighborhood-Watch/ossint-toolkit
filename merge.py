"""Merge two datasets.

This code was specifically created to join data created by gitscrape
with a package-by-country table. The keys are not a perfect match but are
close. 
"""

import time

import pandas as pd


INPUT_FILE_1 = "../processed_data/julia_combined_results_gitscrape_with_underscore_20211107.csv"
INPUT_FILE_2 = "../processed_data/julia_top_10_pkgs_by_country_20211206-092954.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = (
    "../processed_data/merged_" + DATETIME_STAMP + ".csv"
)

df1 = pd.read_csv(INPUT_FILE_1)
df2 = pd.read_csv(INPUT_FILE_2)

df2.columns = ["repo_name", "China", "Russia"]

merge = df1.merge(df2, on='repo_name', how='left')

merge.to_csv(OUTPUT_FILENAME, index=False)