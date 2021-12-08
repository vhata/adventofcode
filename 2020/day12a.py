#!/usr/bin/env python

import sys

instr = []
for r in map(str.strip, sys.stdin):
    instr.append((r[0], int(r[1:])))

# ship starts facing east
fx, fy = 1, 0
# how2turn
turns = {
    (1, 0): ((0, -1), (0, 1)),
    (0, 1): ((1, 0), (-1, 0)),
    (-1, 0): ((0, 1), (0, -1)),
    (0, -1): ((-1, 0), (1, 0)),
}
x, y = 0, 0
for d, v in instr:
    if d == "N":
        y = y - v
    elif d == "S":
        y = y + v
    elif d == "E":
        x = x + v
    elif d == "W":
        x = x - v
    elif d == "L":
        for rt in range(int(v / 90)):
            fx, fy = turns[(fx, fy)][0]
    elif d == "R":
        for rt in range(int(v / 90)):
            fx, fy = turns[(fx, fy)][1]
    elif d == "F":
        x = x + (fx * v)
        y = y + (fy * v)

print(abs(x) + abs(y))
