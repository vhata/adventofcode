#!/usr/bin/env python

import sys

received = {}
for l in sys.stdin:
    n = int(l)
    received[n] = True
    for x in received:
        if received.get(2020 - n - x, False):
            print(n * x * (2020 - n - x))
            break
