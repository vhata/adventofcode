#!/usr/bin/env python

import re
import sys

re_rule = re.compile(r"^([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)")

rules = {}
rule_section = True
for r in map(str.strip, sys.stdin):
    if rule_section:
        m = re_rule.match(r)
        if m:
            rules[m.group(1)] = list(map(int, m.groups()[1:]))
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
    for rule in rules.values():
        if (field >= rule[0] and field <= rule[1]) or (
            field >= rule[2] and field <= rule[3]
        ):
            return True
    return False


valid_tickets = []
for ticket in tickets:
    isvalid = True
    for field in ticket:
        if not valid(field):
            isvalid = False
    if isvalid:
        valid_tickets.append(ticket)

found_rules = {}
while rules.keys():
    matches = 0
    for rule in rules:
        pass
