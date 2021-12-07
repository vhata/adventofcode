#!/usr/bin/env python

from collections import Counter
import sys

adaps = []
for r in map(str.strip, sys.stdin):
    adaps.append(int(r))
adaps = sorted(adaps)


adapcache = {}


def countways(jolts, ads):
    if not ads:
        return 1
    if len(ads) in adapcache:
        return adapcache[len(ads)]
    ways = 0
    for d in range(1, 4):
        for c in range(min(len(ads), 3)):
            if ads[c] == jolts + d:
                ways = ways + countways(ads[c], ads[c + 1 :])
    adapcache[len(ads)] = ways
    return ways


print(countways(0, adaps))
