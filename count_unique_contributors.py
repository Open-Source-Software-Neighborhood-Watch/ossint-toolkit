"""Count unique contributors present in a contributor dataset."""

import time

import pandas as pd

INPUT_FILE = "../processed_data/julia_results_combined_gitgeo-20211108-101909.csv"

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# summarize results by country
num_unique_contributors = df.software_name.nunique()

print(num_unique_contributors)
