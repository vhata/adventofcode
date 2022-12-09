#!/usr/bin/env python3

import sys

DIRS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

headx, heady, tailx, taily = 0, 0, 0, 0
tailpos = set()

def render():
    for y in range(4, -1, -1):
        for x in range(6):
            if (x, y) == (headx, heady):
                print("H", end="")
            elif (x, y) == (tailx, taily):
                print("T", end="")
            else:
                print(".", end="")
        print()
    print()


for r in map(str.strip, sys.stdin):
    dir, num = r.split(None, 1)
    num = int(num)
    for i in range(num):
        headx, heady = headx + DIRS[dir][0], heady + DIRS[dir][1]
        if abs(headx - tailx) > 1 or abs(heady - taily) > 1:
            if abs(headx - tailx) > 0:
                tailx = tailx + (headx - tailx) / abs(headx - tailx)
            if abs(heady - taily) > 0:
                taily = taily + (heady - taily) / abs(heady - taily)
        tailpos.add((tailx, taily))

print(len(tailpos))