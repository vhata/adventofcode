#!/usr/bin/env python

import sys


posns = list(map(int, sys.stdin.readline().strip().split(",")))

minp, maxp = min(posns), max(posns)


def getcost(ps, pos):
    c = 0
    for p in ps:
        c = c + abs(p - pos)
    return c


cost = getcost(posns, maxp + 1)
for i in range(minp, maxp):
    cost = min(cost, getcost(posns, i))

print(cost)
