#!/usr/bin/env python

import math
import sys

ITER = 5

cavemap = []
for r in map(str.strip, sys.stdin):
    cavemap.append(list(map(int, list(r))))

orig_max_x, orig_max_y = len(cavemap[0]), len(cavemap)
max_x, max_y = orig_max_x * ITER - 1, orig_max_y * ITER - 1


def riskgetter(x, y):
    ret = cavemap[y % orig_max_y][x % orig_max_x]

    ret = ret + (y // orig_max_y)
    if ret > 9:
        ret = ret - 9
    ret = ret + (x // orig_max_x)
    if ret > 9:
        ret = ret - 9
    return ret


def getneighbours(x, y):
    neighbours = []
    if x > 0:
        neighbours.append((x - 1, y))
    if y > 0:
        neighbours.append((x, y - 1))
    if x < max_x:
        neighbours.append((x + 1, y))
    if y < max_y:
        neighbours.append((x, y + 1))
    return neighbours


distances = [[(math.inf, False)] * (max_x + 1) for r in range(max_y + 1)]
distances[0][0] = (0, False)

unvisited = set()
unvisited.add((0, 0))
while unvisited:
    x, y = unvisited.pop()
    ns = getneighbours(x, y)
    visited = True
    this_dist = distances[y][x][0]
    for n in ns:
        nx, ny = n
        tent_dist = this_dist + riskgetter(nx, ny)
        if distances[ny][nx][1]:
            continue
        ndist = distances[ny][nx][0]
        if tent_dist < ndist:
            distances[ny][nx] = (tent_dist, False)
        if ndist < this_dist:
            visited = False
        unvisited.add((nx, ny))
    if visited:
        distances[y][x] = (distances[y][x][0], True)

print(distances[max_y][max_x])
