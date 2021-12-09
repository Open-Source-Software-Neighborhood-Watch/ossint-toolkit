"""Count repos countributor-by-contributor in a contributor dataset."""

import time

import pandas as pd

INPUT_FILE = "../processed_data/contributors-from-China-20211108-102558.csv"

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# summarize results by country
num_unique_contributors = df.username.value_counts()

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

print(num_unique_contributors)
