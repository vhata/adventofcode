#!/usr/bin/env python

import sys

dirs = sys.stdin.readline().strip()

moves = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

who = 0
where = [[0, 0], [0, 0]]
houses = set([(0, 0)])
for dir in dirs:
    move = moves[dir]
    where[who][0] = where[who][0] + move[0]
    where[who][1] = where[who][1] + move[1]
    houses.add(tuple(where[who]))
    who = 1 - who

print(len(houses))
