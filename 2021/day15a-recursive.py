#!/usr/bin/env python

import sys
import math
import time

RED = "\033[91m"
GREEN = "\033[92m"
BRIGHT = "\033[1m"
NORM = "\033[00m"

cavemap = []
for r in map(str.strip, sys.stdin):
    cavemap.append(list(map(int, list(r))))

max_x, max_y = len(cavemap[0]) - 1, len(cavemap) - 1


def printroute(route):
    for i in range(max_y + 1):
        for j in range(max_x + 1):
            if (j, i) in route:
                print(f"{BRIGHT}{GREEN}", end="")
            print(cavemap[i][j], end="")
            print(NORM, end="")
        print()
    print()


minrisk = math.inf
foundroute = None


def findroute(risk, route):
    global minrisk, foundroute
    x, y = route[-1]
    if (x, y) == (max_x, max_y):
        if risk < minrisk:
            minrisk, foundroute = risk, route
        return
    if risk >= minrisk and minrisk > 0:
        return
    if x > 0:
        if (x - 1, y) not in route:
            findroute(risk + cavemap[y][x - 1], route + [(x - 1, y)])
    if y > 0:
        if (x, y - 1) not in route:
            findroute(risk + cavemap[y - 1][x], route + [(x, y - 1)])
    if x < max_x:
        if (x + 1, y) not in route:
            findroute(risk + cavemap[y][x + 1], route + [(x + 1, y)])
    if y < max_y:
        if (x, y + 1) not in route:
            findroute(risk + cavemap[y + 1][x], route + [(x, y + 1)])


risk = 0
route = [(0, 0)]
findroute(risk, route)

printroute(foundroute)
print(minrisk)
