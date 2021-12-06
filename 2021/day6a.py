#!/usr/bin/env python

import sys

fish = []
for r in map(str.strip, sys.stdin):
    fish.extend(map(int, r.split(",")))

days = 80
for d in range(days):
    newfish = 0
    nextfish = []
    for f in fish:
        if f == 0:
            nextfish.append(6)
            newfish = newfish + 1
        else:
            nextfish.append(f - 1)
    nextfish.extend([8] * newfish)
    fish = nextfish

print(len(fish))
