#!/usr/bin/env python

import sys

ROCK, PAPER, SCISSORS = "A", "B", "C"

WIN_MAP = { # [to lose, to draw, to win]
    ROCK: [SCISSORS, ROCK, PAPER],
    PAPER: [ROCK, PAPER, SCISSORS],
    SCISSORS: [PAPER, SCISSORS, ROCK],
}

PLAY_POINTS = {ROCK: 1, PAPER: 2, SCISSORS: 3}
GAME_POINTS = [0, 3, 6]

score = 0
for r in map(str.strip, sys.stdin):
    elf_play, desired_outcome_c = r.split(None, 2)
    desired_outcome = ord(desired_outcome_c) - ord('X')

    me_play = WIN_MAP[elf_play][desired_outcome]

    score = score + PLAY_POINTS[me_play]
    score = score + GAME_POINTS[desired_outcome]

print(score)
