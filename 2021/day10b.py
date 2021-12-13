#!/usr/bin/env python

import sys

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 1, "]": 2, "}": 3, ">": 4}

all_scores = []
for line in map(str.strip, sys.stdin):
    stack = []
    corrupt = False
    for c in line:
        if c in pairs.keys():
            stack.append(c)
        else:
            if c != pairs[stack.pop()]:
                corrupt = True
                break
    if not corrupt:
        score = 0
        while stack:
            score = score * 5 + scores[pairs[stack.pop()]]
        all_scores.append(score)

print(sorted(all_scores)[int(len(all_scores) / 2)])
