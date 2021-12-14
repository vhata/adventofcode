#!/usr/bin/env python

from collections import Counter
import sys

polymer = sys.stdin.readline().strip()
sys.stdin.readline()

rules = {}
for rule in map(str.strip, sys.stdin):
    pair, _, ins = rule.split()
    rules[pair] = ins

pairs = Counter()
for i in range(len(polymer) - 1):
    pair = polymer[i : i + 2]
    pairs[pair] = pairs[pair] + 1
counts = Counter(polymer)


def step(pairs, counts):
    newpairs = Counter()
    newcounts = Counter()
    for p in pairs:
        p1 = p[0] + rules[p]
        p2 = rules[p] + p[1]
        newcounts[rules[p]] = newcounts[rules[p]] + pairs[p]
        newpairs[p1] = newpairs[p1] + pairs[p]
        newpairs[p2] = newpairs[p2] + pairs[p]
    # add the old letter counts because we didn't remove any of them
    # don't add the old pair counts, because we replaced them all with the new pairs
    newcounts.update(counts)
    return newpairs, newcounts


for i in range(40):
    pairs, counts = step(pairs, counts)

print(counts.most_common()[0][1] - counts.most_common()[-1][1])
