#!/usr/bin/env python3

import sys
import re

MUL_RE = r"mul\((\d+),(\d+)\)"

total = 0
for r in map(str.strip, sys.stdin):
    for match in re.findall(MUL_RE, r):
        total += int(match[0]) * int(match[1])
        
print(total)