#!/usr/bin/env python

import sys

RACELEN = 2503

SPEED = 0
STAMINA = 1
REST = 2

CYCLEPOS = 0
DIST = 1

deer = {}
for r in map(str.strip, sys.stdin):
    bits = r.split()
    deer[bits[0]] = (int(bits[3]), int(bits[6]), int(bits[13]))

points = dict(zip(deer.keys(), [0] * len(deer)))
race = dict(zip(deer.keys(), [[deer[n][STAMINA], 0] for n in deer]))


def giddyhup():
    for d in deer:
        if race[d][CYCLEPOS] > 0:
            race[d][DIST] = race[d][DIST] + deer[d][SPEED]
        race[d][CYCLEPOS] = race[d][CYCLEPOS] - 1
        if race[d][CYCLEPOS] == -deer[d][REST]:
            race[d][CYCLEPOS] = deer[d][STAMINA]
    windist = max(race[n][DIST] for n in deer)
    for d in deer:
        if race[d][DIST] == windist:
            points[d] = points[d] + 1


for i in range(RACELEN):
    giddyhup()

print(max(points.values()))
