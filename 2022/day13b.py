#!/usr/bin/env python3

from functools import cmp_to_key
import sys

DIVIDER1 = [[2]]
DIVIDER2 = [[6]]


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


packets = sorted(
    [eval(r) for r in map(str.strip, sys.stdin) if r] + [DIVIDER1, DIVIDER2],
    key=cmp_to_key(comp),
    reverse=True,
)

print((packets.index(DIVIDER1) + 1) * (packets.index(DIVIDER2) + 1))
