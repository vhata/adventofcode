#!/usr/bin/env python

from collections import defaultdict
from itertools import permutations
import math
import sys

modifier = {"gain": 1, "lose": -1}
peeps = defaultdict(dict)


def howsad(combo):
    sad = 0
    L = len(combo)
    for i in range(L):
        sad = (
            sad
            + peeps[combo[i]][combo[(i - 1) % L]]
            + peeps[combo[i]][combo[(i + 1) % L]]
        )
    return sad


for r in map(str.strip, sys.stdin):
    who, _, how, much, _, _, _, _, _, _, whomst = r.split()
    peeps[who][whomst.strip(".")] = modifier[how] * int(much)

minsad = -math.inf
for c in permutations(peeps.keys()):
    minsad = max(minsad, howsad(c))

print(minsad)
