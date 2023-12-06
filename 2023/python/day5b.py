#!/usr/bin/env python3

from collections import defaultdict
import math
import sys

seeds = list(map(int, sys.stdin.readline().strip().split(':')[1].split()))
seed_ranges = [seeds[i:i+2] for i in range(0, len(seeds), 2)]

maps = defaultdict(lambda: defaultdict(list))

def getmapping(mapping, srcid):
    for m in mapping:
        if m[1] <= srcid < m[1]+m[2]:
            return m[0] + (srcid - m[1])
    return srcid

mapsrc, mapdst = '', ''
for r in map(str.strip, sys.stdin):
    if not r:
        mapsrc, mapdst = '', ''
        continue
    if ' map:' in r:
        mapsrc, _, mapdst = r.split()[0].split('-')
        continue
    if mapsrc and mapdst:
        maps[mapsrc][mapdst].append(list(map(int, r.split())))

def getlocation(srcid):
    srcmap = 'seed'
    dstmap = list(maps[srcmap].keys())[0]
    while srcmap != 'location':
        dstid = getmapping(maps[srcmap][dstmap], srcid)
        srcid = dstid
        srcmap, dstmap = dstmap, list(maps[srcmap].keys())[0]
    return srcid

def get_seeds(seed_range):
    for i in range(seed_range[0], seed_range[0]+seed_range[1]):
        yield i

minloc = math.inf

for sr in seed_ranges:
    print(sr)
    for x in get_seeds(sr):
        minloc = min(minloc, getlocation(x))
    print(minloc)
    print('-----')

print(minloc)