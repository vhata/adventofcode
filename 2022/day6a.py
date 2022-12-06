#!/usr/bin/env python3

import sys

LEN = 4
for r in map(str.strip, sys.stdin):
    for i in range(len(r)):
        if len(set(r[i : i + LEN])) == LEN:
            print(i + LEN)
            break
