"""Add most recent commit date hash to github repos.

This script enables analysis with the r2c platform.
"""

import json
import time

import pandas as pd
import requests

GITHUB_USERNAME = "jspeed-meyers"
GITHUB_TOKEN = "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"

INPUT_FILENAME = "../data/anaconda_packages_with_github_links_20210810-092234.csv"

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = "../data/github_links_with_most_recent_commit_hash-" + DATETIME_STAMP + ".csv"

# read in data - these are the github links
df = pd.read_csv(INPUT_FILENAME)

# get repo org
df["repo_org"] = df.apply(
    lambda row: row.cleaned_link.split("/")[-2], axis=1
)

# get repo name
df["repo_name"] = df.apply(
    lambda row: row.cleaned_link.split("/")[-1], axis=1
)

# get hash of repo's last commit via GitHub API

def get_most_recent_commit_date(repo_org, repo_name):
    """Extract most recent commit's hashfrom GitHub API.

    Args:
        repo_org (str) - the repository's organization name
        repo_name (str) - the repository's name

    Returns:
        a SHA hash
    """

    # in case no information is found, return error
    date = "ERROR"

    response = requests.get(
            f"https://api.github.com/repos/{repo_org}/{repo_name}/commits",
            auth=(GITHUB_USERNAME, GITHUB_TOKEN),
        )
    if response.ok:
        info = json.loads(response.text or response.content)
        date = info[0]["sha"]

    return date

# get date of last commit
df["commit_last_date"] = df.apply(
    lambda row: get_most_recent_commit_date(row.repo_org, row.repo_name), axis=1
)

# Ensure all rows are printed
pd.set_option("display.max_rows", None)

# export data
df.to_csv(OUTPUT_FILENAME, index=False)
