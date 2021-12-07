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


def checksquare(p, x, y, dx, dy):
    cx = x + dx
    cy = y + dy
    while cy >= 0 and cy < len(p) and cx >= 0 and cx < len(p[cy]) and p[cy][cx] != "L":
        if p[cy][cx] == "#":
            return 1
        cx = cx + dx
        cy = cy + dy
    return 0


def checkneighbours(p, x, y):
    c = 0
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                c = c + checksquare(p, x, y, dx, dy)
    return c


def printneighbours(p):
    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] == ".":
                print(".", end="")
            else:
                print(checkneighbours(p, j, i), end="")
        print()
    print()


def allchange(p):
    newplan = [r[:] for r in p]

    for i in range(len(p)):
        for j in range(len(p[i])):
            if p[i][j] == "L" and checkneighbours(p, j, i) == 0:
                newplan[i][j] = "#"
            if p[i][j] == "#" and checkneighbours(p, j, i) >= 5:
                newplan[i][j] = "L"
    return newplan


oldplan = []
while oldplan != plan:
    oldplan = plan
    plan = allchange(plan)

print(len(list(filter(lambda x: x == "#", chain.from_iterable(plan)))))
