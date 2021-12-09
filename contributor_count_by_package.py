"""Summarize GitGeo .csv results by counting unique countries by package.

Input is a .csv file from GitGeo, which includes a column named 'country.'

Output is terminal output listing packages and unique count of countries.
"""

import pandas as pd

INPUT_FILE = "../data/anaconda_contributors.csv"

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

contributor_count_by_package = df.groupby("software_name")["username"].count()

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

print(contributor_count_by_package)
