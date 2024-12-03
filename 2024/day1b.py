#!/usr/bin/env python3

import sys
from collections import Counter

left, right = [], []

for r in map(str.strip, sys.stdin):
    bits = list(map(int, r.split()))
    left.append(bits[0])
    right.append(bits[1])

counts = Counter(right)

total = 0
for l in left:
    total += l * counts[l]

print(total)