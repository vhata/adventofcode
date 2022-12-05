#!/usr/bin/env python3

import sys

largest = 0
cur = 0
for r in map(str.strip, sys.stdin):
    if not r:
        if largest < cur:
            largest = cur
        cur = 0
    else:
        cur = cur + int(r)
        
if largest < cur:
    largest = cur

print(largest)
