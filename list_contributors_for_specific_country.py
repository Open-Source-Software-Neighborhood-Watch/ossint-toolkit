"""List contributors for only one country.

Input is a .csv file from GitGeo, which includes a column named 'country.'

Output is terminal output listing all contributors associated with a
particular country.
"""

import time

import pandas as pd

COUNTRY_OF_INTEREST = "China"
INPUT_FILE = "../data/top_100_recent_contributors_combined_20210907-1308.csv"

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = (
    "../data/contributors-from-" + COUNTRY_OF_INTEREST + "-" + DATETIME_STAMP + ".csv"
)

# read in GitGeo .csv
df = pd.read_csv(INPUT_FILE, header=0, index_col=False)

# summarize results by country
contributors_for_country_of_interest = df[df.country == COUNTRY_OF_INTEREST]

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

print(contributors_for_country_of_interest)

contributors_for_country_of_interest.to_csv(OUTPUT_FILENAME, index=False)
