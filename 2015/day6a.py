#!/usr/bin/env python

from itertools import chain
import sys

gridsize = 1000
lights = [[0 for x in range(gridsize)] for y in range(gridsize)]

toggle = lambda x: 1 - x
on = lambda _: 1
off = lambda _: 0


def hitit(start, stop, f):
    i, j = start
    ei, ej = stop
    while i <= ei:
        while j <= ej:
            lights[i][j] = f(lights[i][j])
            j = j + 1
        j = start[1]
        i = i + 1


for r in map(str.strip, sys.stdin):
    bits = r[::-1].split()
    start, stop = bits[2][::-1], bits[0][::-1]
    f = None
    if r.startswith("toggle"):
        f = toggle
    elif r.startswith("turn on"):
        f = on
    else:
        f = off
    hitit(list(map(int, start.split(","))), list(map(int, stop.split(","))), f)

print(len(list(filter(lambda x: x == 1, chain.from_iterable(lights)))))
