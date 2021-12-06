#!/usr/bin/env python

from itertools import chain
import sys

x_max, y_max = 0, 0
lines = []
for r in map(str.strip, sys.stdin):
    start, _, finish = r.split()
    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, finish.split(","))
    if x1 == x2 or y1 == y2:
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
    if x1 == x2:
        start = min(y1, y2)
        stop = max(y1, y2) + 1
        for i in range(start, stop):
            ofloor[i][x1] = ofloor[i][x1] + 1
    elif y1 == y2:
        start = min(x1, x2)
        stop = max(x1, x2) + 1
        for j in range(start, stop):
            ofloor[y1][j] = ofloor[y1][j] + 1

print(
    len(
        list(
            filter(lambda x: isinstance(x, int) and x > 1, chain.from_iterable(ofloor))
        )
    )
)
