#!/usr/bin/env python

from collections import Counter
import sys

for r in map(str.strip, sys.stdin):
    nums = list(map(int, r.split(",")))

    endturn = 30000000

    lastsaid = Counter()
    for i, n in enumerate(nums):
        lastsaid[n] = i + 1

    turn = len(nums) + 1
    lastnum = nums[-1]
    lastsaid[lastnum] = 0

    # print(lastsaid)
    while turn <= endturn:
        say = 0
        # print(turn, lastnum, lastsaid[lastnum])
        if lastsaid[lastnum]:
            say = (turn - 1) - lastsaid[lastnum]
        lastsaid[lastnum] = turn - 1
        # print(f"X{say}X")
        lastnum = say
        turn = turn + 1

    print(lastnum)
