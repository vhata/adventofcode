#!/usr/bin/env python3

import sys

grid = []
for r in map(str.strip, sys.stdin):
    grid.append(list(map(int, list(r))))

vis = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (
            (i == 0 or grid[i][j] > max(grid[k][j] for k in range(i)))
            or (j == 0 or grid[i][j] > max(grid[i][k] for k in range(j)))
            or (
                i == len(grid) - 1
                or grid[i][j] > max(grid[k][j] for k in range(i + 1, len(grid)))
            )
            or (
                j == len(grid[i]) - 1
                or grid[i][j] > max(grid[i][k] for k in range(j + 1, len(grid[i])))
            )
        ):
            vis = vis + 1

print(vis)
