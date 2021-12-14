#!/usr/bin/env python

import sys

RED = "\033[91m"
GREEN = "\033[92m"
BRIGHT = "\033[1m"
NORM = "\033[00m"

cave = []
for r in map(str.strip, sys.stdin):
    cave.append(list(map(int, list(r))))


def pcave(c):
    for i in range(len(c)):
        for j in range(len(c[i])):
            if c[i][j] == 0:
                print(BRIGHT, end="")
            print(c[i][j], end="")
            if c[i][j] == 0:
                print(NORM, end="")
        print()
    print()


def flash(x, y):
    cave[y][x] = "X"
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx != 0 or dy != 0:
                step(x + dx, y + dy)


def step(x, y):
    if y < 0 or y >= len(cave):
        return
    if x < 0 or x >= len(cave[y]):
        return
    if cave[y][x] != "X":
        cave[y][x] = cave[y][x] + 1
        if cave[y][x] > 9:
            flash(x, y)


days = 100
flashes = 0
for day in range(days):
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            step(j, i)
    for i in range(len(cave)):
        for j in range(len(cave[i])):
            if cave[i][j] == "X":
                cave[i][j] = 0
                flashes = flashes + 1
print(flashes)
