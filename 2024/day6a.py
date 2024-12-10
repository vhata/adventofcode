#!/usr/bin/env python3

from itertools import chain
import sys

f = open("day6input.txt", "r")
grid: list[list[str]] = []
g_x, g_y = 0, 0
for r in map(str.strip, f):
    if "^" in r:
        g_x, g_y = r.index("^"), len(grid)
    grid.append(list(r))

d_x, d_y = 0, -1


def printgrid():
    print("\n".join(list("".join(grid[y]) for y in range(len(grid)))))
    print(f"({g_x}, {g_y}) [{d_x}, {d_y}]")
    # sys.stdin.readline()


while (
    g_x + d_x >= 0
    and g_x + d_x < len(grid[0])
    and g_y + d_y >= 0
    and g_y + d_y < len(grid)
):
    if grid[g_y + d_y][g_x + d_x] == "#":
        # turn right
        d_x, d_y = -d_y, d_x
    else:
        grid[g_y][g_x] = "X"
        g_x, g_y = g_x + d_x, g_y + d_y
        grid[g_y][g_x] = "^"


grid[g_y][g_x] = "X"

print(len(list(filter(lambda x: x == "X", chain.from_iterable(grid)))))
