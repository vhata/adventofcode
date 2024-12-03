#!/usr/bin/env python3

import sys
import re

MUL_RE = r"(?:(do)\(\))|(?:(mul)\((\d+),(\d+)\))|(?:(don't)\(\))"

total = 0
do = True
for r in map(str.strip, sys.stdin):
    for match in re.findall(MUL_RE, r):
        if "do" in match:
            do = True
        elif "don't" in match:
            do = False
        else:
            if do:
                total += int(match[2]) * int(match[3])
        
print(total)