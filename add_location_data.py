"""Add location data to recent contributors list."""

import time

import pandas as pd

from geolocation import get_contributor_location, get_country_from_location

INPUT_FILENAME = "../data/top_100_recent_contributors_20210903-165846.csv"

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = "../data/top_100_recent_contributors_with_location-" + DATETIME_STAMP + ".csv"

# read in data
# TODO: add skiprows to get later portion
df = pd.read_csv(INPUT_FILENAME, skiprows=range(1, 8500))

# get contributor location for each contributor
df["location"] = df.apply(
    lambda row: get_contributor_location(row.github_login), axis=1
)

# extract country from each contributor location
df["country"] = df.apply(
    lambda row: get_country_from_location(row.location), axis=1
)

# export data
df.to_csv(OUTPUT_FILENAME, index=False)
