#!/usr/bin/env python

import sys


def flydeer(name, secs):
    dist = 0
    speed, stamina, rest = deer[name]
    while secs > 0:
        if secs > stamina:
            secs = secs - stamina
            dist = dist + (stamina * speed)
        else:
            dist = dist + (secs * speed)
            secs = 0
        secs = secs - rest
    return dist


deer = {}
for r in map(str.strip, sys.stdin):
    bits = r.split()
    deer[bits[0]] = (int(bits[3]), int(bits[6]), int(bits[13]))

print(max(flydeer(n, 2503) for n in deer))
