#!/usr/bin/env python

import sys

horiz, depth = 0, 0

for instruc in sys.stdin:
    direc, dist = instruc.split()
    dist = int(dist)
    if direc == "forward":
        horiz = horiz + dist
    if direc == "down":
        depth = depth + dist
    if direc == "up":
        depth = depth - dist

print(horiz * depth)
