#!/usr/bin/env python

import json
import sys


def tally(th):
    if isinstance(th, int):
        return th
    if isinstance(th, str):
        return 0
    if isinstance(th, list):
        return sum(tally(t) for t in th)
    if isinstance(th, dict):
        return sum(tally(th[k]) for k in th)


total = 0
for r in map(str.strip, sys.stdin):
    thing = json.loads(r)
    total = total + tally(thing)

print(total)
