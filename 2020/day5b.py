#!/usr/bin/env python

import sys


maxcol = 127
maxrow = 7


def getseat(card):
    bottom, top = 0, maxcol
    for s in card[:7]:
        if s == "F":
            top = bottom + int((top - bottom) / 2)
        else:  # s == 'B'
            bottom = top - int((top - bottom) / 2)
    assert bottom == top
    row = bottom
    left, right = 0, maxrow
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


highest_seat = maxcol * 8 + maxrow

seats = []

for card in sys.stdin:
    seats.append(getseat(card.strip()))

mine = [s for s in range(min(seats), max(seats)) if s not in seats]
print(mine[0])
