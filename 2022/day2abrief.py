#!/usr/bin/env python3

import sys

score = 0
for r in map(str.strip, sys.stdin):
    elf_play_c, me_play_c = r.split(None, 2)
    elf_play, me_play = ord(elf_play_c) - ord("A"), ord(me_play_c) - ord("X")
    score = score + (me_play + 1) + (((me_play + (1 - elf_play)) % 3) * 3)

print(score)
