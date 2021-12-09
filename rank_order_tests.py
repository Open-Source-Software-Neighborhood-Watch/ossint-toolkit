"""Perform rank-order test on countries.

This analysis came from Tom Pike asking if the drop in China's rank
from the total contributor count to the top 5 contribution count is
meaningful. The question is suprisingly hard to
answer using off the shelf analysis.

The simplest way to answer this query is to say there are 33 countries
in the OSS-INT analysis that have at least fifty contributors.
"""

import pandas as pd

from scipy.stats import mannwhitneyu
from scipy.stats import ranksums

INPUT_FILE = "../excel/contributors_per_pop.xlsx"

# import excel sheet
df = pd.read_excel(open(INPUT_FILE, "rb"), sheet_name="data")

# Perform mann-whitney test to compare rank order
U1, mann_whitney_p = mannwhitneyu(
    df.contrib_rank, df.top_5_contrib_rank, method="exact"
)
print(f"The Mann-Whitney U test p-value is: {mann_whitney_p}")

# Perform wilcoxon rank sum test
ranksum_results = ranksums(df.contrib_rank, df.top_5_contrib_rank)
print(f"The wilcoxon rank sum results are: {ranksum_results}")

# Perform custom permution test-like transformation
df["rank_diff_abs"] = abs(df["contrib_rank"] - df["top_5_contrib_rank"])
print(df["rank_diff_abs"].mean())
print(df["rank_diff_abs"].std())
