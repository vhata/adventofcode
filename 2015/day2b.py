#!/usr/bin/env python

import functools
import itertools
import sys


def getlength(dims):
    lengths = [2 * d[0] + 2 * d[1] for d in itertools.combinations(dims, 2)]
    return min(lengths) + functools.reduce(lambda x, y: x * y, dims, 1)


total = 0
for r in map(str.strip, sys.stdin):
    dims = list(map(int, r.split("x")))
    total = total + getlength(dims)

print(total)
