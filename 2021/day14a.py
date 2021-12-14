#!/usr/bin/env python

from collections import Counter
import sys

polymer = sys.stdin.readline().strip()
sys.stdin.readline()

rules = {}
for rule in map(str.strip, sys.stdin):
    pair, _, ins = rule.split()
    rules[pair] = ins


def step(polymer):
    i = 0
    while i < len(polymer) - 1:
        polymer = polymer[: i + 1] + rules[polymer[i : i + 2]] + polymer[i + 1 :]
        i = i + 2
    return polymer


for i in range(10):
    polymer = step(polymer)

c = Counter(polymer)
print(c.most_common()[0][1] - c.most_common()[-1][1])
