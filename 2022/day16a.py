#!/usr/bin/env python3

import re
import sys

for r in map(str.strip, sys.stdin):
    m = re.match(r"Valve (\S+) has flow rate=(\d+); tunnels lead to valves (?:(DD)(?:, )?)+", r)

nsor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)", r)
    assert m
    sx, sy, bx, by = map(int, m.groups())
