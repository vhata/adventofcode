#!/usr/bin/env python

import re
import sys


def isnice(s):
    if not re.search(r"(..).*\1", s):
        return False
    if not re.search(r"(.).\1", s):
        return False
    return True


nice = 0

for r in map(str.strip, sys.stdin):
    if isnice(r.lower()):
        nice = nice + 1

print(nice)
