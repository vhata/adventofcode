#!/usr/bin/env python

import sys

instr = sys.stdin.readline().strip()

level = 0
dirs = {"(": 1, ")": -1}
for c in instr:
    level = level + dirs[c]

print(level)
