#!/usr/bin/env python3

import sys

DIRS = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, 1),
    "D": (0, -1),
}

NUM_TAILS = 9
tails = [(0, 0) for _ in range(NUM_TAILS + 1)]  # including head
tailpos = set()


def render():
    for y in range(4, -1, -1):
        for x in range(6):
            if (x, y) in tails:
                for i in range(len(tails)):
                    if (x, y) == tails[i]:
                        print(i or "H", end="")
                        break
            else:
                print(".", end="")
        print()
    print()


def chase(hx, hy, tx, ty):
    if abs(hx - tx) > 1 or abs(hy - ty) > 1:
        if abs(hx - tx) > 0:
            tx = tx + (hx - tx) / abs(hx - tx)
        if abs(hy - ty) > 0:
            ty = ty + (hy - ty) / abs(hy - ty)
    return (tx, ty)


for r in map(str.strip, sys.stdin):
    dir, num = r.split(None, 1)
    num = int(num)
    for i in range(num):
        headx, heady = tails[0][0] + DIRS[dir][0], tails[0][1] + DIRS[dir][1]
        tails[0] = (headx, heady)
        for i in range(1, len(tails)):
            tails[i] = chase(tails[i - 1][0], tails[i - 1][1], tails[i][0], tails[i][1])
        tailpos.add((tails[-1][0], tails[-1][1]))

print(len(tailpos))
