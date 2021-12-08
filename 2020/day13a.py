#!/usr/bin/env python

import sys

dtime = int(sys.stdin.readline().strip())
buses = list(
    map(int, filter(lambda x: x != "x", sys.stdin.readline().strip().split(",")))
)

curbuses = buses[:]
while min(curbuses) < dtime:
    for i in range(len(buses)):
        if curbuses[i] < dtime:
            curbuses[i] = curbuses[i] + buses[i]

leaveat = min(curbuses)
print((leaveat - dtime) * buses[curbuses.index(leaveat)])
