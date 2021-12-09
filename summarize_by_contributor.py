"""Summarize GitGeo .csv results by contributor.

Input is a .csv file from GitGeo, which includes a column named 'country.'

Output is terminal output listing the count by contributor.
"""

import time

import pandas as pd

INPUT_FILE = "../data/anaconda_contributors.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FIGURE_FILE = "../figures/contributor_contributions_" + DATETIME_STAMP + ".pdf"

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# summarize results by country
count_by_country = df["username"].value_counts()

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

print(count_by_country)

# create histogram, customize, and save histogram
ax = count_by_country.hist(bins=20)  # set number of histogram bins
ax.set_yscale("log")  # set y-scale to logarithm
ax.set_xlabel("Number of Packages")
ax.set_ylabel("Number of Contributors")
fig = ax.get_figure()
fig.savefig(OUTPUT_FIGURE_FILE)
