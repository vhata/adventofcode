#!/usr/bin/env python

import math
import re
import sys
import time

target = sys.stdin.readline().strip()
m = re.match(
    r"^target area: x=(-?[0-9]+)..(-?[0-9]+), y=(-?[0-9]+)..(-?[0-9]+)", target
)
xmin, xmax, ymin, ymax = map(int, m.groups())
xmin, xmax = min(xmin, xmax), max(xmin, xmax)
ymin, ymax = min(ymin, ymax), max(ymin, ymax)


def maxheight(dx, dy):
    cx, cy = 0, 0
    max_y = -math.inf
    while cx < xmax and cy > ymin and not (dx == 0 and cx < xmin):
        cx = cx + dx
        cy = cy + dy
        if dx != 0:
            dx = (abs(dx) - 1) * (abs(dx) / dx)
        dy = dy - 1
        max_y = max(cy, max_y)
        if cx >= xmin and cx <= xmax and cy >= ymin and cy <= ymax:
            return max_y
    return -math.inf


maxh = -math.inf
solx, soly = None, None

for x in range(1, xmax * 2):  # I made these up
    for y in range(-xmax, xmax):  # And these
        m = maxheight(x, y)
        if m > maxh:
            maxh, solx, soly = m, x, y

print(maxh)
