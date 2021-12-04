#!/usr/bin/env python

import sys

qs = []
count = 0
for q in sys.stdin:
    q = q.strip()
    if not q:
        all_a = qs[0]
        for b in qs[1:]:
            all_a = all_a.intersection(b)
        count = count + len(all_a)
        qs = []
    else:
        qs.append(set(list(q)))

if qs:
    all_a = qs[0]
    for b in qs[1:]:
        all_a = all_a.intersection(b)
    count = count + len(all_a)
print(count)
