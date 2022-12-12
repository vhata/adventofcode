#!/usr/bin/env python3

from ocr import parse
import sys

x = 1
cycle = 0  # we increase the cycle at the beginning of the round, so start at zero

horiz = lambda c: (c-1)%40

def covered(c):
    return abs(horiz(c)-x) < 2

screen = ''

def render():
    global screen
    if covered(cycle):
        screen = screen + '#'
    else:
        screen = screen + '.'

    if not cycle % 40:  # wrap
        screen = screen + '\n'


signal = 0
for r in map(str.strip, sys.stdin):
    # every instruction increases the cycle
    cycle = cycle + 1
    render()

    # "add" instructions increase cycle and add to x, but only after rendering
    if r.startswith('addx'):
        cycle = cycle + 1
        render()
        x = x + int(r[5:])

print(parse(screen))