#!/usr/bin/env python

import re
import string
import sys


def incrpass(s):
    l = list(s)[::-1]
    i = 0
    done = False
    while not done:
        if i == len(s):
            l.append("a")
            done = True
        else:
            l[i] = chr(ord(l[i]) + 1)
            if l[i] == "{":  # the one after 'z'
                l[i] = "a"
                i = i + 1
            else:
                done = True
    return "".join(l[::-1])


def isvalid(s):
    asclow = string.ascii_lowercase
    if not any([asclow[x : x + 3] in s for x in range(len(asclow) - 2)]):
        return False
    if any(c in s for c in ["i", "o", "l"]):
        return False
    if not re.search(r"(.)\1.*(.)\2", s):
        return False
    return True


def optimize(s):
    for i in range(len(s)):
        if s[i] in "iol":
            s = s[:i] + chr(ord(s[i]) + 1) + ("a" * len(s[i + 1 :]))
            break
    return s


password = sys.stdin.readline().strip()
password = incrpass(password)
while not isvalid(password):
    password = incrpass(password)
    password = optimize(password)

print(password)
