#!/usr/bin/env python3

from collections import defaultdict
import sys

seeds = list(map(int, sys.stdin.readline().strip().split(':')[1].split()))
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

srcmap = 'seed'
dstmap = list(maps[srcmap].keys())[0]
srcids = seeds

while srcmap != 'location':
    dstids = []
    for srcid in srcids:
        dstids.append(getmapping(maps[srcmap][dstmap], srcid))
    srcids = dstids
    srcmap, dstmap = dstmap, list(maps[srcmap].keys())[0]

print(min(srcids))