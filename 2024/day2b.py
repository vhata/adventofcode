#!/usr/bin/env python3

import sys


def test_level(level):
    if level[1] == level[0]:
        return False
    cardinality = (level[1] - level[0]) / abs(level[1] - level[0])
    for i in range(1, len(level)):
        distance = cardinality * (level[i] - level[i - 1])
        if distance < 1 or distance > 3:
            return False
    return True


safe = 0
for r in map(str.strip, sys.stdin):
    levels = list(map(int, r.split()))
    assert len(levels) > 1
    if test_level(levels):
        safe += 1
        continue
    for j in range(len(levels)):
        maybe_safe = levels[:j] + levels[j + 1 :]
        if test_level(maybe_safe):
            safe += 1
            break

print(safe)
