#!/usr/bin/env python

import sys

p1pos = int(sys.stdin.readline().strip().split()[-1])
p2pos = int(sys.stdin.readline().strip().split()[-1])


die_count = 0


def detdie():
    global die_count
    n = 1
    while True:
        die_count = die_count + 1
        yield n
        n = (n + 1) % 100


def advance(cur, n):
    cur = cur + n
    while cur > 10:
        cur = cur - 10
    return cur


die = detdie()


def roll():
    return sum(next(die) for i in range(3))


p1sc, p2sc = 0, 0

while p1sc < 1000 and p2sc < 1000:
    p1pos = advance(p1pos, roll())
    p1sc = p1sc + p1pos

    if p1sc >= 1000:
        break

    p2pos = advance(p2pos, roll())
    p2sc = p2sc + p2pos

print(min(p1sc, p2sc) * die_count)
