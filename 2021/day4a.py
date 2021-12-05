#!/usr/bin/env python

from itertools import chain
import sys

calls = list(map(int, sys.stdin.readline().strip().split(",")))
sys.stdin.readline()  # second blank line

boards = [[]]
bnum = 0
for r in map(str.strip, sys.stdin):
    if not r:
        bnum = bnum + 1
        boards.append([])
    else:
        boards[bnum].append(list(map(int, r.split())))
bnum = bnum + 1


def bing(board, c):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == c:
                board[i][j] = "X"
                return


def is_bingo(board):
    for i in range(len(board)):
        all_x = True
        for j in range(len(board[i])):
            if board[i][j] != "X":
                all_x = False
        if all_x:
            return True
    for j in range(len(board[0])):
        all_x = True
        for i in range(len(board)):
            if board[i][j] != "X":
                all_x = False
        if all_x:
            return True
    return False


def score(board):
    return sum(filter(lambda x: x != "X", chain.from_iterable(board)))


for c in calls:
    for b in boards:
        bing(b, c)
        if is_bingo(b):
            print(c * score(b))
            sys.exit(0)
