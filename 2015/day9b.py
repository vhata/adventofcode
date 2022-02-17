#!/usr/bin/env python

from collections import defaultdict
import math
import sys

distcache = {}


def longest(plcs, at):
    key = f"{at}{frozenset(plcs)}"
    if key in distcache:
        return distcache[key]
    long = -math.inf
    plcsleft = plcs - {at}
    if not plcsleft:
        long = 0
    else:
        for x in plcsleft:
            long = max(
                long,
                dists[at][x]
                + longest(
                    plcsleft,
                    x,
                ),
            )
    distcache[key] = long
    return long


dists = defaultdict(dict)

for r in map(str.strip, sys.stdin):
    src, _, dst, _, dist = r.split()
    dists[src][dst] = int(dist)
    dists[dst][src] = int(dist)

print(max([longest(set(dists.keys()), x) for x in dists.keys()]))
