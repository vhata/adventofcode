#!/usr/bin/env python

import sys
import yaml

sue_deets_yaml = """
children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
"""


sue_deets = yaml.safe_load(sue_deets_yaml)

aunts = {}
for r in map(str.strip, sys.stdin):
    this_aunt, deets = r.split(":", 1)
    this_aunt = this_aunt.split()[1]
    aunts[this_aunt] = {}
    for deet in deets.split(","):
        aunts[this_aunt].update(yaml.safe_load(deet))

for aunt in aunts:
    possibility = True
    for deet in sue_deets:
        if deet not in aunts[aunt]:
            continue
        if sue_deets[deet] != aunts[aunt][deet]:
            possibility = False
    if possibility:
        print(aunt)
