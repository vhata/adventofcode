#!/usr/bin/env python

import sys

qs = set()
count = 0
for q in sys.stdin:
    q = q.strip()
    if not q:
        count = count + len(qs)
        qs = set()
    else:
        qs.update(q)

if qs:
    count = count + len(qs)
print(count)
