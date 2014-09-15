# -*- coding: utf- 8 -*-

import csv
from BeautifulSoup import BeautifulSoup
from constants import PATH, TEAMS

def scraping(year, category, division, team):
    players = []

    path = PATH % (year, category, division, team)
    f = open(path)
    html = f.read()
    soup = BeautifulSoup(html)
    rows = soup.findAll('tr', {'class': 'ststats'})

    for row in rows:
        player = [cell.string for cell in row.findAll('td')]
        players.append([year,team,division]+player)

    return players

def get_header(year, category, division, team):
    header = []

    path = PATH % (year, category, division, team)
    f = open(path)
    html = f.read()
    soup = BeautifulSoup(html)
    cols = soup.find(id='stdivmaintbl').findAll('th')

    for col in cols:
        h = ''.join([content.encode("utf8") for content in col.contents 
                        if content.string])
        header.append(h.replace("　", ""))
    header = ["年度", "チーム", "部"] + header

    return header

if __name__ == "__main__":
    years = range(2005, 2015)
    stats_b = []
    stats_p = []

    header_flg = False
    for year in years:
        print year

        for team in TEAMS[year]:
            stats_b += scraping(year, 'b', 1, team)
            stats_b += scraping(year, 'b', 2, team)
            stats_p += scraping(year, 'p', 1, team)
            if not header_flg:
                header_b = get_header(year, 'b', 1, team)
                header_p = get_header(year, 'p', 1, team)

    header_b = map(lambda s: s.replace("｜", "ー"), header_b)
    header_p = map(lambda s: s.replace("｜", "ー"), header_p)

    writer = csv.writer(open("batting.csv", "w"), lineterminator="\n")
    writer.writerow(header_b)
    writer.writerows(stats_b)

    writer = csv.writer(open("pitching.csv", "w"), lineterminator="\n")
    writer.writerow(header_p)
    writer.writerows(stats_p)
