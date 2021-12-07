#!/usr/bin/env python

from collections import Counter
import sys

adaps = []
for r in map(str.strip, sys.stdin):
    adaps.append(int(r))
adaps = sorted(adaps)

jolts = 0
diffs = Counter()
for n in adaps:
    diffs[n - jolts] = diffs[n - jolts] + 1
    jolts = n
diffs[3] = diffs[3] + 1

print(diffs[1] * diffs[3])
