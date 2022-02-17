#!/usr/bin/env python

import re
import sys

DOUBLESLASH = "\\\\"
SINGLESLASH = "!"  # so as not to confuse later things looking for other escapes
SLASHQUOTE = '\\"'
SINGLEQUOTE = '"'
totalcode = 0
totalval = 0
for r in map(str.strip, sys.stdin):
    totalcode = totalcode + len(r)
    r = r[1:-1]
    r = r.replace(DOUBLESLASH, SINGLESLASH).replace(SLASHQUOTE, SINGLEQUOTE)
    while m := re.search(r"\\x(..)", r):
        r = r.replace(m.group(0), chr(int(m.group(1), base=16)))
    totalval = totalval + len(r)

print(totalcode - totalval)
