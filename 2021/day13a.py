#!/usr/bin/env python

from itertools import chain
import sys

dots = []
max_x, max_y = 0, 0
for r in map(str.strip, sys.stdin):
    if not r:
        break
    x, y = list(map(int, r.split(",")))
    dots.append([x, y])
    max_x = max(x, max_x)
    max_y = max(y, max_y)

max_x, max_y = max_x + 1, max_y + 1
paper = [[None] * max_x for c in range(max_y)]
for dot in dots:
    paper[dot[1]][dot[0]] = "#"


def ppaper(p):
    for i in range(len(p)):
        for j in range(len(p[i])):
            if not p[i][j]:
                print(".", end="")
            else:
                print("#", end="")
        print()
    print()


def foldpaper(v, c):
    if v == "y":
        new_y = c
        newpaper = [paper[c] for c in range(c)]
        for i in range(c + 1, max_y):
            for j in range(max_x):
                if paper[i][j]:
                    newpaper[c - (i - c)][j] = paper[i][j]
        return newpaper, max_x, new_y
    else:
        new_x = c
        newpaper = [row[:c] for row in paper]
        for i in range(max_y):
            for j in range(c + 1, max_x):
                if paper[i][j]:
                    newpaper[i][c - (j - c)] = paper[i][j]
        return newpaper, new_x, max_y


for r in map(str.strip, sys.stdin):
    v, c = r.split()[2].split("=")
    c = int(c)
    paper, max_x, max_y = foldpaper(v, c)
    break

print(len(list(filter(lambda x: x, chain.from_iterable(paper)))))
