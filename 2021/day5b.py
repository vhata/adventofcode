#!/usr/bin/env python

from itertools import chain
import sys

x_max, y_max = 0, 0
lines = []
for r in map(str.strip, sys.stdin):
    start, _, finish = r.split()
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, finish.split(","))
    x_max = max(x_max, x1, x2)
    y_max = max(y_max, y1, y2)
    lines.append(((x1, y1, x2, y2)))

x_max = x_max + 1
y_max = y_max + 1

ofloor = []
for i in range(y_max):
    ofloor.append([0] * x_max)


def pboard():
    for i in range(y_max):
        for j in range(x_max):
            print(str(ofloor[i][j]).replace("0", "."), end=" ")
        print()


for line in lines:
    x1, y1, x2, y2 = line
    dx = 0 if x1 == x2 else int((x2 - x1) / abs(x2 - x1))
    dy = 0 if y1 == y2 else int((y2 - y1) / abs(y2 - y1))
    while x1 != x2 or y1 != y2:
        ofloor[y1][x1] = ofloor[y1][x1] + 1
        x1 = x1 + dx
        y1 = y1 + dy
    # ranges are inclusive, so:
    ofloor[y1][x1] = ofloor[y1][x1] + 1

print(
    len(
        list(
            filter(lambda x: isinstance(x, int) and x > 1, chain.from_iterable(ofloor))
        )
    )
)
