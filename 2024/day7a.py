#!/usr/bin/env python3

import sys

day = 7
f = sys.stdin
f = open(f"day{day}input.txt", "r")
f = open(f"day{day}sample.txt", "r")


def gencalc(bits):
    if len(bits) == 1:
        yield bits[0]
    else:
        for i in gencalc(bits[1:]):
            yield bits[0] + i
            yield bits[0] * i


total = 0

for r in map(str.strip, f):
    val_s, bits_s = r.split(":")
    val = int(val_s)
    bits = list(map(int, bits_s.split()))
    bits = bits[::-1]  # left-to-right evaluation
    if val in gencalc(bits):
        total += val

print(total)
