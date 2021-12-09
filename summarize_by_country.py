"""Summarize GitGeo .csv results by country.

Input is a .csv file from GitGeo, which includes a column named 'country.'

Output is terminal output listing the count by country.
"""

import pandas as pd

INPUT_FILE = "../data/top_100_recent_contributors_combined_20210907-1308.csv"

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# summarize results by country
count_by_country = df["country"].value_counts()

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

print(count_by_country)
