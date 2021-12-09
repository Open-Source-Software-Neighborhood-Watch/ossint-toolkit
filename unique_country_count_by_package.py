"""Summarize GitGeo .csv results by counting unique countries by package.

Input is a .csv file from GitGeo, which includes a column named 'country.'

Output is terminal output listing packages and unique count of countries.
"""

import time

import pandas as pd

INPUT_FILE = "../data/anaconda_contributors.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FIGURE_FILE = "../figures/unique_country_count_" + DATETIME_STAMP + ".pdf"

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

unique_country_count_by_package = df.groupby("software_name")["country"].nunique()

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

print(unique_country_count_by_package.mean())

# create histogram, customize, and save histogram
ax = unique_country_count_by_package.hist(bins=20)  # set number of histogram bins
# ax.set_yscale("log")  # set y-scale to logarithm
ax.set_xlabel("Number of Unique Countries")
ax.set_ylabel("Number of Packages")
fig = ax.get_figure()
fig.savefig(OUTPUT_FIGURE_FILE)
