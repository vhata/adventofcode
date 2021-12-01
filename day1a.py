#!/usr/bin/env python

import sys

prev = int(sys.stdin.readline())

count = 0
for line in sys.stdin:
    if int(line) > prev:
        count = count + 1
    prev = int(line)

print(count)
