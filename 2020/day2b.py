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
    first, second, letter, passwd = m.groups()
    first, second = int(first), int(second)

    if (passwd[first - 1] == letter) ^ (passwd[second - 1] == letter):
        valid = valid + 1

print(valid)
