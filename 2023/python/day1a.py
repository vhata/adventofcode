#!/usr/bin/env python3

import re
import sys

total = 0

for r in map(str.strip, sys.stdin):
    # use regex to find the first and last digits in the string
    # and convert them to integers
    m = re.match(r'^[^0-9]*([0-9])', r)
    assert m
    first = m.group(1)
    m = re.search(r'([0-9])[^0-9]*$', r)
    assert m
    last = m.group(1)
    total = total + int(f'{first}{last}')

print(total)


