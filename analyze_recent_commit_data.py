"""Analyze recent commit data, identifying top X contributors per repo

For the "Jackie Kazil" analysis
"""

import time

import pandas as pd

NUM_TOP_CONTRIBUTORS = 10000

INPUT_FILENAME = "../data/recent_contributors-20210903-154716.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = (
    "../data/top_"
    + str(NUM_TOP_CONTRIBUTORS)
    + "_recent_contributors_"
    + DATETIME_STAMP
    + ".csv"
)

df = pd.read_csv(INPUT_FILENAME)

# Note: pay attention to whether the analysis requires grouping by
# GitHub handle, repo name, or both
count = df.groupby(["github_login"]).size() # "repo" 

count_df = count.to_frame(name="size").reset_index()

# analysis 
sorted_df = count_df.sort_values(["size"], ascending=[False])

# only use .head if the analysis needs to focus on the top X contributors
#top_contribs = sorted_df.groupby("size").head(NUM_TOP_CONTRIBUTORS)

sorted_df.to_csv(OUTPUT_FILENAME, index=False)
