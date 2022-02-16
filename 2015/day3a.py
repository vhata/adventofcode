#!/usr/bin/env python

import sys

dirs = sys.stdin.readline().strip()

moves = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

x, y = 0, 0
houses = set([(x, y)])
for dir in dirs:
    move = moves[dir]
    x = x + move[0]
    y = y + move[1]
    houses.add((x, y))

print(len(houses))
