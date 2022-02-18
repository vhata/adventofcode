#!/usr/bin/env python

import sys


def looksay(s):
    i = 0
    res = ""
    while i < len(s):
        ch = s[i]
        co = 1
        i = i + 1
        while i < len(s) and s[i] == ch:
            i = i + 1
            co = co + 1
        res = res + f"{co}{ch}"
    return res


s = sys.stdin.readline().strip()
for i in range(40):
    s = looksay(s)

print(len(s))
