#!/usr/bin/env python3

import sys

left, right = [], []

for r in map(str.strip, sys.stdin):
    bits = list(map(int, r.split()))
    left.append(bits[0])
    right.append(bits[1])

left = sorted(left)
right = sorted(right)

total = 0

for l, r in zip(left, right):
    total += abs(l - r)

print(total)

