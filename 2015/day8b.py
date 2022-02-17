#!/usr/bin/env python

import re
import sys

DOUBLESLASH = "\\\\"
SINGLESLASH = "\\"
SLASHQUOTE = '\\"'
SINGLEQUOTE = '"'

origcode = 0
newcode = 0
for r in map(str.strip, sys.stdin):
    origcode = origcode + len(r)
    r = r.replace(SINGLESLASH, DOUBLESLASH).replace(SINGLEQUOTE, SLASHQUOTE)
    r = f'"{r}"'
    newcode = newcode + len(r)

print(newcode - origcode)
