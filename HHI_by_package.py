"""Summarize GitGeo .csv results by counting unique countries by package.

Input is a .csv file from GitGeo, which includes a column named 'country.'

Output is terminal output listing packages and their Herfindahl-Hirschman Index

https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_Index
"""

# WORK IN PROGRESS

import pandas as pd

INPUT_FILE = "../data/combined.csv"

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# drop all entries without a country
# df =

# calculate hhi by package
package_by_country = df.groupby("software_name")["country"]
# df.groupby(['state', 'office_id']).agg({'sales': 'sum'})
# then calculate percentages
# then apply formula
# hhi_by_package =

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

print(hhi_by_package)
