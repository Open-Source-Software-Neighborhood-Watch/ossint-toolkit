"""Summarize most recent commit data via histogram

Input is a .csv file with commit dates'

Output is terminal output listing the count by contributor.
"""

import time

from datetime import datetime
import pandas as pd


INPUT_FILE = "../data/github_links_with_most_recent_commit_date-20210920-114948.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FIGURE_FILE = "../figures/most_recent_commit_histogram_" + DATETIME_STAMP + ".pdf"

df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# filter out rows with ERROR in commit time column
df = df[df["commit_last_date"] != "ERROR"]

# calculate days from now until most recent commits
date_format = "%Y-%m-%dT%H:%M:%SZ"
now = datetime.now()
df["days_since_last_commit"] = df.apply(
    lambda row: (now - datetime.strptime(row["commit_last_date"], date_format)).days, axis=1
)

# create histogram, customize, and save histogram

ticks = [365 * x for x in range(0, 10)]

ax = df["days_since_last_commit"].hist(bins=ticks)  # set number of histogram bins
#ax.set_yscale("log")  # set y-scale to logarithm
ax.set_xlabel("Days Since Last Commit")
ax.set_ylabel("Number of Packages")
ax.set_xticks(ticks)
fig = ax.get_figure()
fig.savefig(OUTPUT_FIGURE_FILE)
