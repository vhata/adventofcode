#!/usr/bin/env python

import sys

code = []
for r in map(str.strip, sys.stdin):
    code.append(r.split())
    # turn operand into integer
    code[-1][1] = int(code[-1][1])
    # add visit count
    code[-1].append(0)


def terminates(stack):
    acc = 0
    ip = 0
    while ip < len(stack) and stack[ip][2] == 0:
        stack[ip][2] = stack[ip][2] + 1
        if stack[ip][0] == "jmp":
            ip = ip + stack[ip][1]
        else:  # nop or acc
            if stack[ip][0] == "acc":
                acc = acc + stack[ip][1]
            ip = ip + 1
    if ip >= len(stack):
        return (True, acc)
    return (False, 0)


corruption = {"jmp": "nop", "nop": "jmp"}
for i, line in enumerate(code):
    if line[0] in corruption.keys():
        codecopy = [c[:] for c in code]
        codecopy[i][0] = corruption[codecopy[i][0]]
        terms, acc = terminates(codecopy)
        if terms:
            print(acc)
            break
