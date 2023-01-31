#!/usr/bin/env python3

import math
import re
import sys

MAX_COORD = 4000000


def mhdist(x1, y1, x2, y2) -> int:
    return abs(x1 - x2) + abs(y1 - y2)


def nobeacons(sx, sy, bx, by, y):
    d = mhdist(sx, sy, bx, by)
    return (sx-(d-abs(sy-y)), sx+(d-abs(sy-y)))

def rmrange(possibs, nopes):
    if nopes[0] > nopes[1]:
        return possibs
    newpossibs = []
    for poss in possibs:
        if nopes[0] > poss[1] or nopes[1] < poss[0]:  # no overlap
            newpossibs.append(poss)
        elif nopes[0] > poss[0] and nopes[1] < poss[1]:  # nopes contained by poss
            newpossibs.append((poss[0],nopes[0]-1)) # left chunk
            newpossibs.append((nopes[1]+1, poss[1])) # right chunk
        elif nopes[0] <= poss[0] and nopes[1] >= poss[1]:  # nopes overwrites poss
            continue
        elif nopes[0] <= poss[0] and nopes[1] < poss[1]:  # nopes overwrites left part
            newpossibs.append((nopes[1]+1, poss[1]))
        elif nopes[0] > poss[0] and nopes[1] >= poss[1]:  # nopes overwrites right part
            newpossibs.append((poss[0], nopes[0]-1))
    return newpossibs

possibility = dict(zip(range(MAX_COORD), [[(0,MAX_COORD)]]*MAX_COORD))

i = 0
for r in map(str.strip, sys.stdin):
    i = i + 1
    m = re.match(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", r
    )
    assert m
    sx, sy, bx, by = map(int, m.groups())
    d = mhdist(sx, sy, bx, by)
    for y in range(sy-d, sy+d):
        if y in possibility:
            newposs = rmrange(possibility[y], nobeacons(sx, sy, bx, by, y))
            if newposs:
                possibility[y] = newposs
            else:
                del possibility[y]

assert len(possibility) == 1
y = list(possibility.keys())[0]
assert len(possibility[y]) == 1
assert possibility[y][0][0] == possibility[y][0][1]
x = possibility[y][0][0]
print(x*4000000 + y)