#!/usr/bin/env python

import sys

aim, horiz, depth = 0, 0, 0

for instruc in sys.stdin:
    direc, dist = instruc.split()
    dist = int(dist)
    if direc == "forward":
        horiz = horiz + dist
        depth = depth + (dist * aim)
    if direc == "down":
        aim = aim + dist
    if direc == "up":
        aim = aim - dist

print(horiz * depth)
