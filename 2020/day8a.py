#!/usr/bin/env python

import sys

code = []
for r in map(str.strip, sys.stdin):
    code.append(r.split())
    # turn operand into integer
    code[-1][1] = int(code[-1][1])
    # add visit count
    code[-1].append(0)

acc = 0
ip = 0
while code[ip][2] == 0:
    code[ip][2] = code[ip][2] + 1
    if code[ip][0] == "jmp":
        ip = ip + code[ip][1]
    else:  # nop or acc
        if code[ip][0] == "acc":
            acc = acc + code[ip][1]
        ip = ip + 1

print(acc)
