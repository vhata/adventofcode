#!/usr/bin/env python

import re
import sys

overlaps = 0
for r in map(str.strip, sys.stdin):
    m = re.match(r"^(\d+)-(\d+),(\d+)-(\d+)", r)
    assert m
    p1a, p1b, p2a, p2b = [int(p) for p in m.groups()]
    if (p1a >= p2a and p1b <= p2b) or (p2a >= p1a and p2b <= p1b):
        overlaps = overlaps + 1

print(overlaps)
