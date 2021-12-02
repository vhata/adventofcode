#!/usr/bin/env python

import sys


def getseat(card):
    bottom, top = 0, 127
    for s in card[:7]:
        if s == "F":
            top = bottom + int((top - bottom) / 2)
        else:  # s == 'B'
            bottom = top - int((top - bottom) / 2)
    assert bottom == top
    row = bottom
    left, right = 0, 7
    for s in card[7:]:
        if s == "L":
            right = left + int((right - left) / 2)
        else:  # s =='R'
            left = right - int((right - left) / 2)
    assert left == right
    col = left
    seat = row * 8 + col
    # print(row, col, seat)
    return seat


highest = 0
for card in sys.stdin:
    seat = getseat(card.strip())
    highest = max(highest, seat)

print(highest)
