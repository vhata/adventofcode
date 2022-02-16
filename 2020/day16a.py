#!/usr/bin/env python

import re
import sys

re_rule = re.compile(r"^[a-z ]+: (\d+)-(\d+) or (\d+)-(\d+)")

rules = []
rule_section = True
for r in map(str.strip, sys.stdin):
    if rule_section:
        m = re_rule.match(r)
        if m:
            rules.append(list(map(int, m.groups())))
        else:
            break

# "your ticket:"
sys.stdin.readline()
my_ticket = list(map(int, sys.stdin.readline().strip().split(",")))
sys.stdin.readline()  # blank line

# "nearby tickets:"
sys.stdin.readline()
tickets = []
for r in map(str.strip, sys.stdin):
    tickets.append(list(map(int, r.split(","))))


def valid(field):
    for rule in rules:
        if (field >= rule[0] and field <= rule[1]) or (
            field >= rule[2] and field <= rule[3]
        ):
            return True
    return False


invalid_fields = []
for ticket in tickets:
    for field in ticket:
        if not valid(field):
            invalid_fields.append(field)

print(sum(invalid_fields))
