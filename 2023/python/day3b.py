#!/usr/bin/env python3

import sys
from collections import defaultdict
from functools import reduce

def printgrid(grid):
    for row in grid:
        print(row)


def getgears(grid, i, j):
    neargears = []
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            if x < 0 or y < 0:
                continue
            if x >= len(grid) or y >= len(grid[i]):
                continue
            if grid[x][y] == '*':
                neargears.append((x, y))
    return neargears
    

grid = [list(r.strip()) for r in sys.stdin]

inanumber = False
number = ''

gears = defaultdict(list)
thisnumbergears = set()

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in '1234567890':
            inanumber = True
            number += grid[i][j]
            for gear in getgears(grid, i, j):
                thisnumbergears.add(gear)
        else:
            if inanumber:
                for gear in thisnumbergears:
                    gears[gear].append(int(number))
                inanumber = False
                thisnumbergears = set()
                number = ''
    if inanumber:
        for gear in thisnumbergears:
            gears[gear].append(int(number))
        inanumber = False
        thisnumbergears = set()
        number = ''

gearsums = 0
for gear in gears:
    if len(gears[gear]) > 1:
        gearsums += reduce(lambda x, y: x * y, gears[gear], 1)

print(gearsums)