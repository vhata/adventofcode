#!/usr/bin/env python

import sys

instr = sys.stdin.readline().strip()

level = 0
dirs = {"(": 1, ")": -1}
for i, c in enumerate(instr):
    level = level + dirs[c]
    if level == -1:
        break

print(i + 1)
