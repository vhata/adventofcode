#!/usr/bin/env python

import sys

mmap = []
for r in sys.stdin:
    mmap.append(r.strip())

x, y = 0, 0
trees = 0
while y < len(mmap):
    if mmap[y][x] == "#":
        trees = trees + 1
    x = (x + 3) % len(mmap[0])
    y = y + 1

print(trees)
