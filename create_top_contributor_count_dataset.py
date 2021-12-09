"""Create dataset of top X Anaconda package contributors.

Take as input a .csv with all Anaconda package contributors.
This script assumes that the contributors are ordered by most
commits to least commits. The script then keeps only those
top X contributors, where X is defined by the user.

This script enables analysis of the top contributors to a
set of packages, a population that is relatively involved with
a project and not simply providing "drive-by" commits.
"""

import time

import pandas as pd

# number of top contributors to perform filtering
TOP_CONTRIB_NUM = 5

INPUT_FILE = "../data/anaconda_contributors.csv"
DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = (
    "../data/top_"
    + str(TOP_CONTRIB_NUM)
    + "_contributors_anaconda_"
    + DATETIME_STAMP
    + ".csv"
)


# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# keep only the number of top contributors associated with each package
filter_df = df.groupby("software_name").head(TOP_CONTRIB_NUM)

filter_df.to_csv(OUTPUT_FILENAME, index=False)
