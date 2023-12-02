#!/usr/bin/env python3

import sys

totals = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

ans = 0
for r in map(str.strip, sys.stdin):
    gameid, handfulls = r.split(':')
    id = int(gameid.split()[1])
    possible = True
    for hand in map(str.strip, handfulls.split(';')):
        for col in map(str.strip, hand.split(',')):
            count, color = col.split()
            if totals[color] < int(count):
                possible = False
                break
    if possible:
        ans = ans + id

print(ans)