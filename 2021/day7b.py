#!/usr/bin/env python

import sys


posns = list(map(int, sys.stdin.readline().strip().split(",")))

minp, maxp = min(posns), max(posns)


def getcost(ps, pos, maxcost=None):
    c = 0
    for p in ps:
        dist = abs(p - pos)
        c = c + (dist * (dist + 1)) / 2
        if maxcost and c >= maxcost:
            return maxcost
    return c


cost = getcost(posns, maxp + 1)
for i in range(minp, maxp):
    cost = getcost(posns, i, cost)

print(cost)
