# -*- coding: utf- 8 -*-

URL = "http://bis.npb.or.jp/%s/stats/id%s%s_%s.html"
PATH = "./html/%s/id%s%s_%s.html"

teams_latest = ['g', 't', 'c', 'd', 'db', 's',
                'e', 'l', 'm', 'h', 'bs', 'f']
teams_until_2011 = ['d', 's', 'g', 't', 'c', 'yb',
                     'h', 'f', 'l', 'bs', 'e', 'm']

TEAMS = {}

for year in range(2005, 2012):
    TEAMS[year] = teams_until_2011

for year in range(2012, 2014):
    TEAMS[year] = teams_latest

