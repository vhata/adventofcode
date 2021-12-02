#!/usr/bin/env python

import re
import sys

p = re.compile(
    r"^(\d+)-(\d+) (.): (.*)$",
)

valid = 0
for rule in sys.stdin:
    m = p.match(rule)
    if not m:
        raise Exception("broken input")
    min, max, letter, passwd = m.groups()
    min, max = int(min), int(max)
    tot = 0
    for c in passwd:
        if c == letter:
            tot = tot + 1
    if tot >= min and tot <= max:
        valid = valid + 1

print(valid)
