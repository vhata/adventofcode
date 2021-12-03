#!/usr/bin/env python

import sys

# unfortunately going to have to store all the numbers
numstore = []

for num in sys.stdin:
    numstore.append(num.strip())

# store them several times in fact :(
oxygen, co2 = numstore[:], numstore[:]

for i in range(len(numstore[0])):
    if len(oxygen) > 1:
        o_zeroes, o_ones = 0, 0
        for num in oxygen:
            if num[i] == "0":
                o_zeroes = o_zeroes + 1
            else:
                o_ones = o_ones + 1
        if o_ones >= o_zeroes:
            oxygen = list(filter(lambda s: s[i] == "1", oxygen))
        else:
            oxygen = list(filter(lambda s: s[i] == "0", oxygen))
    if len(co2) > 1:
        c_zeroes, c_ones = 0, 0
        for num in co2:
            if num[i] == "0":
                c_zeroes = c_zeroes + 1
            else:
                c_ones = c_ones + 1
        if c_zeroes <= c_ones:
            co2 = list(filter(lambda s: s[i] == "0", co2))
        else:
            co2 = list(filter(lambda s: s[i] == "1", co2))
    if len(oxygen) == 1 and len(co2) == 1:
        break

print(int(oxygen[0], 2) * int(co2[0], 2))
