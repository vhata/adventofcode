#!/usr/bin/env python

import sys

badges = []

g = []
for r in map(str.strip, sys.stdin):
    g.append(r)
    if len(g) == 3:
        only = set(g[0])
        for bag in g[1:]:
            only = only.intersection(bag)
        badge = list(only)[0]
        if badge < 'a':
            badge = chr(ord('z') + ord(badge) - ord('A') + 1)
        badges.append(badge)
        g = []

print(sum(ord(e)-ord('a')+1 for e in badges))

