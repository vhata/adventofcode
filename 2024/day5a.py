#!/usr/bin/env python3

import sys

# f = sys.stdin
f = open("day5input.txt", "r")
rules = []
for r in map(str.strip, f):
    if not r:
        break
    rules.append(list(map(int, r.split("|"))))

updates = []
for r in map(str.strip, f):
    updates.append(list(map(int, r.split(","))))

total = 0
for u in updates:
    correct = True
    for rule in rules:
        try:
            if u.index(rule[0]) > u.index(rule[1]):
                correct = False
                break
        except ValueError:
            continue
    if correct:
        total += u[len(u) // 2]

print(total)
