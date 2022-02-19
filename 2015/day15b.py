#!/usr/bin/env python

from itertools import combinations
from functools import reduce
from collections import defaultdict
import sys

greds = defaultdict(dict)
features = []
calories = dict()

for r in map(str.strip, sys.stdin):
    bits = r.split()
    ing = bits[0].strip(":")
    for i in [2, 4, 6, 8]:
        feature = bits[i - 1]
        features.append(feature)
        greds[ing][feature] = int(bits[i].strip(","))
    calories[ing] = int(bits[10])


def nomness(amounts):
    noms = {}
    for feat in features:
        noms[feat] = sum(amounts[ing] * greds[ing][feat] for ing in amounts)
        if noms[feat] < 0:
            noms[feat] = 0

    calness = sum(amounts[ing] * calories[ing] for ing in amounts)
    if calness != 500:
        return -1
    return reduce(lambda x, y: x * y, noms.values(), 1)


def getamounts():
    spoons = 100
    ingredients = greds.keys()
    # This is taken from u/drakehutner on Reddit
    return [
        (
            {
                i: b - a - 1
                for i, a, b in zip(
                    ingredients, (-1,) + c, c + (spoons + len(ingredients) - 1,)
                )
            }
        )
        for c in combinations(
            range(spoons + len(ingredients) - 1), len(ingredients) - 1
        )
    ]


print(max(nomness(a) for a in getamounts()))
