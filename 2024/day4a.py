#!/usr/bin/env python3

import sys

XMAS = "XMAS"

f = open("day4input.txt", "r")
grid = []
for r in map(str.strip, f):
    grid.append(list(r))


def testgrid_in_direction(i, j, di, dj) -> bool:
    xmas = 0
    while 0 <= i < len(grid) and 0 <= j < len(grid[i]) and xmas < 4:
        if grid[i][j] != XMAS[xmas]:
            return False
        i += di
        j += dj
        xmas += 1
    if xmas == 4:
        return True
    return False


def testgrid(i, j) -> int:
    this_xmas = 0
    this_xmas += sum(
        testgrid_in_direction(i, j, dx, dy)
        for dx in range(-1, 2)
        for dy in range(-1, 2)
        if (dx, dy) != (0, 0)
    )
    return this_xmas


totalxmas = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "X":
            totalxmas += testgrid(i, j)

print(totalxmas)
