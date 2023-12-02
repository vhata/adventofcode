#!/usr/bin/env python3

import sys

total_power = 0
for r in map(str.strip, sys.stdin):
    mins = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    gameid, handfulls = r.split(':')
    id = int(gameid.split()[1])
    for hand in map(str.strip, handfulls.split(';')):
        for col in map(str.strip, hand.split(',')):
            count, color = col.split()
            if mins[color] < int(count):
                mins[color] = int(count)
    pow = mins['red'] * mins['green'] * mins['blue']
    total_power = total_power + pow

print(total_power)