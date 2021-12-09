"""
"""

import time

import pandas as pd

INPUT_FILE = "../data/top_10000_recent_contributors_20210917-104147.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FIGURE_FILE = "../figures/commit_count_power_law_" + DATETIME_STAMP + ".pdf"

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

df.reset_index()

ax = df.hist(column="size", range=[0, 1500], bins=50, log=True, title='')

ax[0][0].set_ylabel("Contributor Count")
ax[0][0].set_xlabel("Number of Commits")
ax[0][0].figure.savefig(OUTPUT_FIGURE_FILE)
