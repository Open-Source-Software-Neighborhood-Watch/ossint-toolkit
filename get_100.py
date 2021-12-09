# Retrieve top 100 most download PyPI packages
# Big thanks to hugovk

# Usage: place inside pypi-scan folder and
# use 'python get_100.py' to generate a json output

from scrapers import get_top_packages

top_100 = get_top_packages(top_n=100)

print(top_100)
