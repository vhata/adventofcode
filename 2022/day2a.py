#!/usr/bin/env python3

import sys

ROCK, PAPER, SCISSORS = "X", "Y", "Z"
ELF_TO_ME = {"A": "X", "B": "Y", "C": "Z"}

WINNERS = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}

PLAY_POINTS = {ROCK: 1, PAPER: 2, SCISSORS: 3}
LOSE, DRAW, WIN = 0, 3, 6

score = 0
for r in map(str.strip, sys.stdin):
    elf_play_c, me_play = r.split(None, 2)
    elf_play = ELF_TO_ME[elf_play_c]

    score = score + PLAY_POINTS[me_play]

    if me_play == WINNERS[elf_play]:
        score = score + WIN
    elif me_play == elf_play:
        score = score + DRAW

print(score)
