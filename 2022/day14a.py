#!/usr/bin/env python3

import sys

START_X, START_Y = 500, 0

obst = set()
max_y = 0

for r in map(str.strip, sys.stdin):
    bits = r.split(" -> ")
    for i in range(1, len(bits)):
        x1, y1 = map(int, bits[i - 1].split(","))
        x2, y2 = map(int, bits[i].split(","))

        max_y = max(max_y, y1, y2)

        dx, dy = x2 - x1, y2 - y1
        steps = max(abs(dx), abs(dy))
        x_inc, y_inc = dx / steps, dy / steps
        for i in range(steps + 1):
            obst.add((x1, y1))
            x1, y1 = x1 + x_inc, y1 + y_inc

filling = True
units = 0
while filling:
    sand_x, sand_y = START_X, START_Y
    falling = True
    while falling:
        next_x, next_y = sand_x, sand_y + 1  # down
        if (next_x, next_y) in obst:
            next_x = next_x - 1  # down to the left
        if (next_x, next_y) in obst:
            next_x = next_x + 2  # down to the right
        if (next_x, next_y) in obst:
            obst.add((sand_x, sand_y))  # at rest
            units = units + 1
            falling = False
        elif next_y >= max_y:
            falling = filling = False
        sand_x, sand_y = next_x, next_y

print(units)
