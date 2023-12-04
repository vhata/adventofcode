#!/usr/bin/env python3

import sys

def printgrid(grid):
    for row in grid:
        print(row)


def checksymbol(grid, i, j):
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            if x == i and y == j:
                continue
            if x < 0 or y < 0:
                continue
            if x >= len(grid) or y >= len(grid[i]):
                continue
            if grid[x][y] not in '1234567890.':
                return True
    return False
    

grid = [list(r.strip()) for r in sys.stdin]

inanumber = False
number = ''
isapart = False

partssum = 0

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] in '1234567890':
            inanumber = True
            number += grid[i][j]
            isapart = isapart or checksymbol(grid, i, j)
        else:
            if inanumber:
                if isapart:
                    partssum += int(number)
                inanumber = False
                number = ''
                isapart = False
    if inanumber:
        if isapart:
            partssum += int(number)
        inanumber = False
        number = ''
        isapart = False

print(partssum)