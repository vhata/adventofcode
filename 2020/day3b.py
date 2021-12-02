#!/usr/bin/env python

import sys

mmap = []
for r in sys.stdin:
    mmap.append(r.strip())


def c_slope(dx, dy):
    x, y = 0, 0
    trees = 0
    while y < len(mmap):
        if mmap[y][x] == "#":
            trees = trees + 1
        x = (x + dx) % len(mmap[0])
        y = y + dy
    return trees


slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
treecheck = 1
for s in slopes:
    treecheck = treecheck * c_slope(s[0], s[1])

print(treecheck)
