#!/usr/bin/env python

import sys

pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}

score = 0
for line in map(str.strip, sys.stdin):
    stack = []
    for c in line:
        if c in pairs.keys():
            stack.append(c)
        else:
            if c != pairs[stack.pop()]:
                score = score + scores[c]
                break

print(score)
