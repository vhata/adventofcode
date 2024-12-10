#!/usr/bin/env python3

import sys

day = 7
f = sys.stdin
f = open(f"day{day}sample.txt", "r")
f = open(f"day{day}input.txt", "r")

for r in map(str.strip, f):
