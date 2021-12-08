#!/usr/bin/env python

import re
import sys

re_mask = re.compile(r"^mask = ([X01]+)")
cmd_mask = re.compile(r"^mem\[(\d+)\] = (\d+)")

mask = []
memory = {}
for r in map(str.strip, sys.stdin):
    m = re_mask.match(r)
    if m:
        mask = [(i, int(c)) for i, c in enumerate(list(m.group(1)[::-1])) if c != "X"]
        continue
    m = cmd_mask.match(r)
    if m:
        addr, value = map(int, m.groups())
        for pos, val in mask:
            if val:
                value = value | (1 << pos)
            else:
                value = value & ~(1 << pos)
        memory[addr] = value

print(sum(memory.values()))
