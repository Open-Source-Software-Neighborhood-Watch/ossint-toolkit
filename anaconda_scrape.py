"""Scrape anaconda package names and corresponding github links.

User provides a URL to the anaconda page that contains the package information
for one particular python version, e.g. 3.9, and for one particular platform,
e.g. linux 64. This program then extracts all the package names and associated
links (provided by Anaconda) for each package. This data is then exported
to a csv.
"""

import csv

from bs4 import BeautifulSoup
import requests

URL = "https://docs.anaconda.com/anaconda/packages/py3.9_linux-64/"

if __name__ == "__main__":

    # retrieve specified URL
    page = requests.get(URL)

    # convert html to BeautifulSoup object to make navigation easy
    soup = BeautifulSoup(page.content, "html.parser")

    # filter down to the package table
    table = soup.find(lambda tag: tag.name == "table")

    # identify all table cells with a link
    pkgs = table.find_all(lambda tag: "href" in tag.attrs)

    # create name for csv file that contains the exported results
    python_version_and_platform = URL.split("/")[-2]
    output_name = "packages_name_links_" + python_version_and_platform + ".csv"

    # write results to csv file
    with open(output_name, "w", newline="") as csvfile:

        # create csv file
        fieldnames = ["package_name", "anaconda_link"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        # create header row of csv file
        writer.writerow(
            {"package_name": "package_name", "anaconda_link": "anaconda_link"}
        )

        # loop through each package, writing out the package name and the URL link
        # provided by anaconda.
        for pkg in pkgs:
            writer.writerow({"package_name": pkg.string, "anaconda_link": pkg["href"]})
