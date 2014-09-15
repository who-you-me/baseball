# -*- coding: utf- 8 -*-

import os
import argparse
import urllib
import random
import time
from constants import URL, PATH, TEAMS

def fetch(year, category, division, team):
    url = URL % (year, category, division, team)
    path = PATH % (year, category, division, team)
    print url
    urllib.urlretrieve(url, path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
            description="fetch patting and pitching stats page from npb site"
    )
    parser.add_argument("--from", type=int, dest="from_year")
    parser.add_argument("--to", type=int, dest="to_year")

    args = parser.parse_args()
    from_year = args.from_year or 2005
    to_year = args.to_year or 2014

    if not os.path.exists("html"):
        os.mkdir("html")

    for year in range(from_year, to_year + 1):
        year_path = os.path.join("html", str(year))
        if not os.path.exists(year_path):
            os.mkdir(year_path)

        for team in TEAMS[year]:
            for stat in [(bp, div) for bp in ["b", "p"] for div in [1, 2]]:
                fetch(year, stat[0], stat[1], team)
                interval = 1 + random.random()
                time.sleep(interval)

