"""Filter in packages with a GitHub link.

Take as input a .csv file with a field called clean_link, then
output only those values that include https://github.com. Also make sure
all GitHub links are unique.

The ouput should be a .txt file, each github link on its own line.
"""

import time

import pandas as pd

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
INPUT_FILENAME = "../data/cleaned_packages_name_links_py3.9_linux-64.csv"
OUTPUT_FILENAME = "../data/only_packages_with_github_links_" + DATETIME_STAMP + ".csv"

# open input file and store in pandas dataframe
df = pd.read_csv(INPUT_FILENAME, header=0, index_col=False)

# filter in only rows with a link to a GitHub repo
df_filtered = df[df["cleaned_link"].str.contains("https://github.com", na=False)]

# make sure all GitHub links are unique
df_filtered = df_filtered.drop_duplicates(subset=["cleaned_link"], keep="first")

# export filtered dataset to csv file
df_filtered.to_csv(OUTPUT_FILENAME, columns=["cleaned_link"], index=False)
