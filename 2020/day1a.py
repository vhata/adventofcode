#!/usr/bin/env python

import sys

received = {}
for l in sys.stdin:
    n = int(l)
    received[n] = True
    if received.get(2020 - n, False):
        print(n * (2020 - n))
