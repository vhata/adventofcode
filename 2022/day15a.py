#!/usr/bin/env python3

import math
import re
import sys

Y_ROW = 2000000

def mhdist(x1, y1, x2, y2) -> int:
    return abs(x1-x2) + abs(y1-y2)

def nobeacons(sx, sy, bx, by):
    d = mhdist(sx, sy, bx, by)
    return [x for x in range(sx-d, sx+d+1) if mhdist(sx, sy, x, Y_ROW) <= d]

sensors = {}
beacons = set()
minx, maxx = math.inf, -math.inf

empty_x = set()

for r in map(str.strip, sys.stdin):
    m = re.match(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", r)
    assert m
    sx, sy, bx, by = map(int, m.groups())
    empty_x.update(nobeacons(sx, sy, bx, by))
    beacons.add((bx, by))

for b in beacons:
    if b[1] == Y_ROW:
        empty_x.discard(b[0])

print(len(empty_x))