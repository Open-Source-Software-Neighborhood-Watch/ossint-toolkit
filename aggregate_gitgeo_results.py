"""Conver all *.csv files associated a GitGeo run into a single csv."""

import glob
import time

import pandas as pd

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = (
    "../processed_data/julia_results_combined_gitgeo-"
    + DATETIME_STAMP
    + ".csv"
)

# the path to the folder storing the csv files that are to be combined
INPUT_PATH = "../raw_data/gitgeo_results"
all_csv_files = glob.glob(INPUT_PATH + "/*.csv")

li = []

for filename in all_csv_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)

frame.to_csv(OUTPUT_FILENAME, index=False)