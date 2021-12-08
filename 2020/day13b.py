#!/usr/bin/env python

from functools import reduce
import sys

# discard leave time
sys.stdin.readline()

# this problem requires "chinese remainder theorem" and
# nobody got time for that
# stolen from https://0xdf.gitlab.io/adventofcode2020/13
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


for r in map(str.strip, sys.stdin):
    schedule = list(map(lambda x: x != "x" and int(x) or x, r.split(",")))
    buses = list(filter(lambda x: x != "x", schedule))
    offsets = [int(b) - i for i, b in enumerate(schedule) if b != "x"]
    print(chinese_remainder(buses, offsets))

    continue

    # original solution here
    schedule = list(map(lambda x: x != "x" and int(x) or x, r.split(",")))
    print(schedule)

    time = min(filter(lambda x: x != "x", schedule))
    works = False
    while not works:
        works = True
        for i, bus in enumerate(schedule):
            if bus != "x":
                if (time % bus) != ((bus - i) % bus):
                    works = False
        time = time + 1
    print(time)
