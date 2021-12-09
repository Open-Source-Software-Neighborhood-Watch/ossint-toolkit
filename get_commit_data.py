"""Get handles from recent commits associated with GitHub repos.

This is really the "Jackie Kazil" analysis. At one research meeting
she raised the point that there is an important temporal component
to commit data. If GitGeo-like analyses are done on all commits, the
temporal component is missing. This script therefore allows the analyst
to specify a time window and analyze commits to GitHub repos since
that time window.

Return .csv of repo, github_login for all recent commits
"""

import csv
import json
import time

import requests

DATETIME_STAMP = time.strftime("%Y%m%d-%H%M%S")
OUTPUT_FILENAME = "../data/recent_contributors-" + DATETIME_STAMP + ".csv"
GITHUB_USERNAME = "jspeed-meyers"
GITHUB_TOKEN = "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"

# read in github repo list
GITHUB_FILE = "../data/anaconda_packages_with_github_links_20210810-092234.csv"
with open(GITHUB_FILE, newline="") as f:
    reader = csv.reader(f)
    # ignore first row, which is a header
    next(reader)
    githubs = list(reader)

# create csv file
with open(OUTPUT_FILENAME, "w", newline="") as csvfile:

    # add first row to csv
    fieldnames = ["repo", "github_login"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({"repo": "repo", "github_login": "github_login"})

    for github in githubs:

        # extract GitHub repo ower and repo name
        owner = github[0].split("/")[-2]
        repo = github[0].split("/")[-1]

        # loop over the pages of commits associated with a repo
        for page in range(1, 100):
            response = requests.get(
                "https://api.github.com/repos/"
                + f"{owner}/"
                + f"{repo}/"
                + "commits"
                + f"?page={page}"
                + "&per_page=100"
                + "&since=2020-09-03",  # beginning of time window
                auth=(str(GITHUB_USERNAME), str(GITHUB_TOKEN)),
            )

            if response.ok:
                commits = json.loads(response.text or response.content)

            for commit in commits:
                try:
                    login = commit["author"]["login"]
                    writer.writerow({"repo": repo, "github_login": login})
                except (TypeError, KeyError) as error:
                    print(f"Error: {error}")

            # break out of loop if no more pagination
            if "next" not in response.links:
                break
