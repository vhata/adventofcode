#!/usr/bin/env python3

import sys

x = 1
cycle = 0

important = lambda c: c == 20 or (c - 20) % 40 == 0

signal = 0
for r in map(str.strip, sys.stdin):
    # every instruction increases the cycle
    cycle = cycle + 1

    # check if we pass an important one
    if important(cycle):
        signal = signal + (cycle*x)

    # add instructions increase cycle and x
    if r.startswith('addx'):
        cycle = cycle + 1
        # check if we pass an important one
        if important(cycle):
            signal = signal + (cycle*x)
        x = x + int(r[5:])


print(signal)