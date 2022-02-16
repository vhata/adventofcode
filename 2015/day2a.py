#!/usr/bin/env python

import itertools
import sys


def getarea(dims):
    areas = [d[0] * d[1] for d in itertools.combinations(dims, 2)]
    smallest = min(areas)
    area = sum(areas) * 2 + smallest
    return area


total = 0
for r in map(str.strip, sys.stdin):
    dims = list(map(int, r.split("x")))
    total = total + getarea(dims)

print(total)
