#!/usr/bin/env python3

from collections import defaultdict
from math import ceil
import sys

stacks = defaultdict(lambda: [])

loading_stacks = True
for r in sys.stdin:
    if loading_stacks:
        if not '[' in r:
            loading_stacks = False
            continue

        for i in range(1, len(r), 4):
            if r[i] != ' ':
                stacks[ceil(i/4)].append(r[i])
    else:
        if not r.startswith('move'):
            continue
        
        _, num, _, src, _, dst = r.split()
        num, src, dst = map(int, [num, src, dst])
        for i in range(num):
            stacks[dst].insert(0, stacks[src].pop(0))

msg = ''
for k in sorted(stacks.keys()):
    if stacks[k]:
        msg = msg + stacks[k][0]

print(msg)


