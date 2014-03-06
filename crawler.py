# -*- coding: utf- 8 -*-

import sys, os
import urllib
from constants import URL, PATH, TEAMS

def crawl_npb(year, category, division, team):
    url = URL % (year, category, division, team)
    path = PATH % (year, category, division, team)
    print url
    urllib.urlretrieve(url, path)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        years = range(2005, 2014)
    elif len(sys.argv) == 2:
        years = [int(sys.argv[1])]
    else:
        years = range(int(sys.argv[1]), int(sys.argv[2])+1)

    if not os.path.exists("html"):
        os.mkdir("html")

    for year in years:
        if not os.path.exists("html/"+str(year)):
            os.mkdir("html/"+str(year))

        for team in TEAMS[year]:
            crawl_npb(year, 'b', 1, team)
            crawl_npb(year, 'b', 2, team)
            crawl_npb(year, 'p', 1, team)
            crawl_npb(year, 'p', 2, team)

