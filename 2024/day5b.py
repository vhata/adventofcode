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
    correct = False
    fu = u[::]
    while not correct:
        correct = True
        for rule in rules:
            try:
                if fu.index(rule[0]) > fu.index(rule[1]):
                    correct = False
                    fu.remove(rule[0])
                    fu.insert(fu.index(rule[1]), rule[0])
                    break
            except ValueError:
                continue
    if fu != u:
        total += fu[len(fu) // 2]

print(total)
