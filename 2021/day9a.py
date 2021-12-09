#!/usr/bin/env python

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


risk = 0
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
            risk = risk + v + 1
print(risk)
