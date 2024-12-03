#!/usr/bin/env python3

import sys

safe = 0
for r in map(str.strip, sys.stdin):
    levels = list(map(int, r.split()))
    assert len(levels) > 1
    if(levels[1] == levels[0]):
        # unsafe
        continue
    cardinality = (levels[1] - levels[0])/abs(levels[1] - levels[0])
    unsafe = False
    for i in range(1, len(levels)):
        distance = cardinality * (levels[i] - levels[i-1])
        if distance < 1 or distance > 3:
            unsafe = True
            break
    if not unsafe:
        safe += 1

print(safe)
    