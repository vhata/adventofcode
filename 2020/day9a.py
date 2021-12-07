#!/usr/bin/env python

import sys

nums = []
for r in map(str.strip, sys.stdin):
    nums.append(int(r))

winsize = 25
for n in range(winsize, len(nums)):
    preamble = sorted(nums[n - winsize : n])
    found = False
    for x in preamble:
        if (nums[n] - x) in preamble:
            found = True
            break
        if (nums[n] - x) < x:
            break
    if not found:
        print(nums[n])
        sys.exit(0)
