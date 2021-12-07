#!/usr/bin/env python

import sys

nums = []
for r in map(str.strip, sys.stdin):
    nums.append(int(r))

invalidindex = -1
invalidnum = -1
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
        invalidindex = n
        invalidnum = nums[n]
        break

for n in range(invalidindex):
    for m in range(n + 2, invalidindex):
        if sum(nums[n:m]) == invalidnum:
            print(min(nums[n:m]) + max(nums[n:m]))
            sys.exit(0)
        if n - m > winsize:
            break
