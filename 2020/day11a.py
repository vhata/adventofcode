#!/usr/bin/env python

from itertools import chain
import sys

plan = []
for r in map(str.strip, sys.stdin):
    plan.append(list(r))


def pplan(p):
    for r in p:
        print("".join(r))
    print()


def allchange(p):
    def checksquare(x, y):
        if y < 0 or y >= len(p):
            return 0
        if x < 0 or x >= len(p[y]):
            return 0
        return 1 if p[y][x] == "#" else 0

    def checkneighbours(x, y):
        c = 0
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx != 0 or dy != 0:
                    c = c + checksquare(x + dx, y + dy)
        return c

    newplan = [r[:] for r in p]

    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] == "L" and checkneighbours(j, i) == 0:
                newplan[i][j] = "#"
            if p[i][j] == "#" and checkneighbours(j, i) >= 4:
                newplan[i][j] = "L"
    return newplan


oldplan = []
while oldplan != plan:
    oldplan = plan
    plan = allchange(plan)

print(len(list(filter(lambda x: x == "#", chain.from_iterable(plan)))))
