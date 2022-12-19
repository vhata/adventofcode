#!/usr/bin/env python3

from itertools import islice
from math import inf
import sys


def getpair():
    while r := list(islice(sys.stdin, 3)):
        yield r


def comp(a, b):
    isnum = lambda x: isinstance(x, (int, float))

    a1, b1 = a, b

    # rule 1
    if isnum(a1) and isnum(b1):
        # -1, 0, or 1, because bools are ints and have their own arithmetic
        return (b1 - a1 > 0) - (b1 - a1 < 0)

    # rule 3
    if isnum(a1):
        ax = [a1]
    else:
        ax = a1[::]
    if isnum(b1):
        bx = [b1]
    else:
        bx = b1[::]

    # rule 2
    # make sure that if left runs out first, it'll "win" for all the rest of right's elements
    # ax = ax + [-inf] * (max(len(bx) - len(ax), 0))

    while ax and bx:
        r = comp(ax.pop(0), bx.pop(0))
        if r:
            return r

    if bx:
        return 1
    if ax:
        return -1
    return 0


print(sum(i + 1 for i, c in enumerate(getpair()) if comp(eval(c[0]), eval(c[1])) > 0))
