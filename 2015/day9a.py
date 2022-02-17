#!/usr/bin/env python

from collections import defaultdict
import math
import sys

distcache = {}


def shortest(plcs, at):
    key = f"{at}{frozenset(plcs)}"
    if key in distcache:
        return distcache[key]
    short = math.inf
    plcsleft = plcs - {at}
    if not plcsleft:
        short = 0
    else:
        for x in plcsleft:
            short = min(
                short,
                dists[at][x]
                + shortest(
                    plcsleft,
                    x,
                ),
            )
    distcache[key] = short
    return short


dists = defaultdict(dict)

for r in map(str.strip, sys.stdin):
    src, _, dst, _, dist = r.split()
    dists[src][dst] = int(dist)
    dists[dst][src] = int(dist)

print(min([shortest(set(dists.keys()), x) for x in dists.keys()]))
