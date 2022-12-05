#!/usr/bin/env python

import sys

extras = []
for r in map(str.strip, sys.stdin):
    extra = list(set(r[:len(r)/2]).intersection(set(r[len(r)/2:])))[0]
    if extra < 'a':
        extra = chr(ord('z') + ord(extra) - ord('A') + 1)
    extras.append(extra)

print(sum(ord(e)-ord('a')+1 for e in extras))

