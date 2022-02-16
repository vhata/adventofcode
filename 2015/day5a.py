#!/usr/bin/env python

from collections import Counter
import string
import sys

vowels = "aeiou"
bad = ["ab", "cd", "pq", "xy"]


def isnice(s):
    c = Counter(s)
    vs = sum([c[v] for v in vowels])
    if vs < 3:
        return False
    double = False
    for l in string.ascii_lowercase:
        if l * 2 in s:
            double = True
    if not double:
        return False
    if any([b in s for b in bad]):
        return False
    return True


nice = 0

for r in map(str.strip, sys.stdin):
    if isnice(r.lower()):
        nice = nice + 1

print(nice)
