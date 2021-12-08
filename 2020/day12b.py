#!/usr/bin/env python

import sys

instr = []
for r in map(str.strip, sys.stdin):
    instr.append((r[0], int(r[1:])))

wx, wy = 10, -1
x, y = 0, 0
for d, v in instr:
    if d == "N":
        wy = wy - v
    elif d == "S":
        wy = wy + v
    elif d == "E":
        wx = wx + v
    elif d == "W":
        wx = wx - v
    elif d == "L":
        for rt in range(int(v / 90)):
            wx, wy = wy, -wx
    elif d == "R":
        for rt in range(int(v / 90)):
            wx, wy = -wy, wx
    elif d == "F":
        x = x + (wx * v)
        y = y + (wy * v)

print(abs(x) + abs(y))
