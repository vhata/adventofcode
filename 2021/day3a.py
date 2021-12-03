#!/usr/bin/env python

import sys

zeroes, ones = [], []
for num in sys.stdin:
    num = num.strip()
    if not zeroes:
        zeroes = [0] * len(num)
        ones = [0] * len(num)
    for i, c in enumerate(num):
        if c == "0":
            zeroes[i] = zeroes[i] + 1
        elif c == "1":
            ones[i] = ones[i] + 1

gamma, epsilon = 0, 0
for i in range(len(zeroes)):
    if ones[i] > zeroes[i]:
        gamma = (gamma * 2) + 1
        epsilon = epsilon * 2
    else:
        gamma = gamma * 2
        epsilon = (epsilon * 2) + 1

print(gamma * epsilon)
