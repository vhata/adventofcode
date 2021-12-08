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
        ones = [i for i, c in enumerate(list(m.group(1)[::-1])) if c == "1"]
        exes = [i for i, c in enumerate(list(m.group(1)[::-1])) if c == "X"]
        continue
    m = cmd_mask.match(r)
    if m:
        addr, value = map(int, m.groups())
        for pos in ones:
            addr = addr | (1 << pos)
        addrs = [addr]
        for ex in exes:
            newaddrs = []
            for a in addrs:
                newaddrs.append(a | (1 << ex))
                newaddrs.append(a & ~(1 << ex))
            addrs = newaddrs
        for addr in addrs:
            memory[addr] = value

print(sum(memory.values()))
