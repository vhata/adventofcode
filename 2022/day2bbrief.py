#!/usr/bin/env python3

import sys

score = 0
for r in map(str.strip, sys.stdin):
    elf_play_c, me_strat_c = r.split(None, 2)
    elf_play, me_strat = ord(elf_play_c) - ord("A"), ord(me_strat_c) - ord("X")
    me_play = (me_strat + (elf_play - 1)) % 3
    score = score + (me_play + 1) + (((me_play + (1 - elf_play)) % 3) * 3)

print(score)
