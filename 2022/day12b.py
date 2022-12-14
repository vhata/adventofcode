#!/usr/bin/env python3

from collections import deque
import string
import sys

AZ = string.ascii_lowercase

grid = []


def bfs(grid, pos, dest):
    w, h = len(grid[0]), len(grid)
    q = deque([[pos]])
    seen = set([pos])
    while q:
        path = q.popleft()
        x, y = path[-1]
        if (x, y) == dest:
            return path

        e = AZ.index(grid[y][x])

        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < w and 0 <= y2 < h and (x2, y2) not in seen:
                e2 = AZ.index(grid[y2][x2])
                if e2 <= e + 1:
                    q.append(path + [(x2, y2)])
                    seen.add((x2, y2))
    return []


dest = (0, 0)
starts = []
for r in map(str.strip, sys.stdin):
    grid.append([])
    for i, c in enumerate(r):
        if c == "S":
            c = "a"
        grid[-1].append(c)
        if c == "a":
            starts.append((i, len(grid) - 1))
        if c == "E":
            dest = (i, len(grid) - 1)
            grid[-1][-1] = "z"

lens = []
for s in starts:
    p = bfs(grid, s, dest)
    if p:
        lens.append(len(p) - 1)

print(min(lens))
