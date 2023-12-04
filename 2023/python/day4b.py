#!/usr/bin/env python3

import sys
from collections import defaultdict

wins = defaultdict(int)

card = 1
for r in map(str.strip, sys.stdin):
    numbers = r.split(':')[1]
    winners, mine = map(set, map(str.split, numbers.split('|')))
    mywinners = winners & mine
    wins[card] = wins[card] + 1
    for i in range(card + 1, card + len(mywinners) + 1):
        wins[i] = wins[i] + wins[card]
    card = card + 1

print(sum(wins.values()))