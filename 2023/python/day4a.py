#!/usr/bin/env python3

import sys

worth = 0

for r in map(str.strip, sys.stdin):
    numbers = r.split(':')[1]
    winners, mine = map(set, map(str.split, numbers.split('|')))
    mywinners = winners & mine
    if len(mywinners) > 0:
        worth = worth + (1 << len(mywinners)-1)

print(worth)