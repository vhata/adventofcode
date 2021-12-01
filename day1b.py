#!/usr/bin/env python

import sys

windowsize = 3
window = []
for i in range(windowsize):
    window.append(int(sys.stdin.readline()))
prev = sum(window)

count = 0
for line in sys.stdin:
    window = window[1:] + [int(line)]
    if sum(window) > prev:
        count = count + 1
    prev = sum(window)

print(count)
