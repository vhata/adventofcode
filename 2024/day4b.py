#!/usr/bin/env python3

import sys

XMAS = {
    "M": "S",
    "S": "M",
    "A": False,
    "X": False,
}

f = open("day4input.txt", "r")
grid = []
for r in map(str.strip, f):
    grid.append(list(r))


def testgrid(i, j) -> int:
    if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[i]) - 1:
        return 0
    if (
        grid[i - 1][j - 1] == XMAS[grid[i + 1][j + 1]]
        and grid[i - 1][j + 1] == XMAS[grid[i + 1][j - 1]]
    ):
        return 1
    return 0


totalxmas = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "A":
            totalxmas += testgrid(i, j)

print(totalxmas)
