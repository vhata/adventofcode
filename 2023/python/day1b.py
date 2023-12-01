#!/usr/bin/env python3

import re
import sys

total = 0

digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six':6,
          'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
DIGIT_MATCH = f'([0-9]|{"|".join(digits.keys())})'
FIRST_MATCH = f'^.*?({DIGIT_MATCH})'
LAST_MATCH = f'.*({DIGIT_MATCH}).*$'
FIRST_RE = re.compile(FIRST_MATCH)
LAST_RE = re.compile(LAST_MATCH)

for r in map(str.strip, sys.stdin):
    first = re.match(FIRST_RE, r)
    assert first
    last = re.search(LAST_RE, r)
    assert last
    first_d = digits.get(first.group(1), first.group(1))
    last_d = digits.get(last.group(1), last.group(1))
    total = total + int(f'{first_d}{last_d}')

print(total)


