#!/usr/bin/env python3

from functools import reduce
import sys

grid = []
for r in map(str.strip, sys.stdin):
    grid.append(list(map(int, list(r))))

high_scenic = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        def takeuntil(lam, l):  # because takewhile isn't enough
            done = False
            for n in l:
                if not done:
                    yield (n)
                if lam(n):
                    done = True
        getscene = lambda l: len(list(takeuntil(lambda x: x>=grid[i][j], l)))

        scenes = [
            getscene(s) for s in [
                [grid[k][j] for k in range(i)][::-1],
                [grid[i][k] for k in range(j)][::-1],
                [grid[k][j] for k in range(i+1, len(grid))],
                [grid[i][k] for k in range(j+1, len(grid[i]))],
            ]
        ]
        high_scenic = max(high_scenic, reduce(lambda a, b: a * b, scenes))

print(high_scenic)
