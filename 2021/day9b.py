#!/usr/bin/env python

import math
import sys

heightmap = []
for r in map(str.strip, sys.stdin):
    heightmap.append(list(map(int, list(r))))


def islower(x, y, val):
    if y < 0 or y >= len(heightmap):
        return True
    if x < 0 or x >= len(heightmap[y]):
        return True
    if val < heightmap[y][x]:
        return True
    return False


def lowsurrounds(x, y, excl, c=0):
    basin = excl.copy()
    basin.add((x, y))
    if y < 0 or y >= len(heightmap):
        return []
    if x < 0 or x >= len(heightmap[y]):
        return []
    if heightmap[y][x] == 9:
        return []
    if (x - 1, y) not in basin:
        basin.update(lowsurrounds(x - 1, y, basin, c + 1))
    if (x + 1, y) not in basin:
        basin.update(lowsurrounds(x + 1, y, basin, c + 1))
    if (x, y - 1) not in basin:
        basin.update(lowsurrounds(x, y - 1, basin, c + 1))
    if (x, y + 1) not in basin:
        basin.update(lowsurrounds(x, y + 1, basin, c + 1))
    return basin


def findbasin(x, y):
    basin = set()
    basin.add((x, y))
    basin.update(lowsurrounds(x, y, basin))
    return len(basin)


basins = []
for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        lowpoint = False
        v = heightmap[i][j]
        if (
            islower(j - 1, i, v)
            and islower(j + 1, i, v)
            and islower(j, i - 1, v)
            and islower(j, i + 1, v)
        ):
            lowpoint = True
        if lowpoint:
            basins.append(findbasin(j, i))


print(math.prod(sorted(basins)[-3:]))
