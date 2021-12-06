#!/usr/bin/env python

from collections import Counter
import sys

fish = Counter(map(int, sys.stdin.readline().strip().split(",")))

days = 256
for d in range(days):
    newfish = fish[0]
    for age in range(8):
        fish[age] = fish[age + 1]
    fish[6] = fish[6] + newfish
    fish[8] = newfish

print(sum(fish.values()))
