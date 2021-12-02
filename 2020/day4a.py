#!/usr/bin/env python

import sys

fields = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
    # "cid",
]


def validate(p):
    reqd = set(fields)
    passpt = " ".join(p).split()
    for field in passpt:
        f = field.split(":")[0]
        if f in reqd:
            reqd.remove(f)
    if reqd:
        return 0
    return 1


cur_pass = []
valid = 0
for r in sys.stdin:
    r = r.strip()
    if not r:
        valid = valid + validate(cur_pass)
        cur_pass = []
    else:
        cur_pass.append(r)

if cur_pass:
    valid = valid + validate(cur_pass)

print(valid)
