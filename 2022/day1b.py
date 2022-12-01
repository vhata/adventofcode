#!/usr/bin/env python

import sys

largest = [0,0,0]
cur = 0
for r in map(str.strip, sys.stdin):
    if not r:
        if largest[0] < cur:
            largest = sorted(largest[1:] + [cur])
        cur = 0
    else:
        cur = cur + int(r)
        
if largest[0] < cur:
    largest = sorted(largest[1:] + [cur])

print(sum(largest))
