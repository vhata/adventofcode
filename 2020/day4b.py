#!/usr/bin/env python

import re
import sys


def validate_height(s):
    if s[-2:] == "cm":
        l = int(s[:-2])
        if l >= 150 and l <= 193:
            return True
    if s[-2:] == "in":
        l = int(s[:-2])
        if l >= 59 and l <= 76:
            return True
    return False


fields = {
    "byr": lambda s: len(s) == 4 and int(s) >= 1920 and int(s) <= 2002,
    "iyr": lambda s: len(s) == 4 and int(s) >= 2010 and int(s) <= 2020,
    "eyr": lambda s: len(s) == 4 and int(s) >= 2020 and int(s) <= 2030,
    "hgt": validate_height,
    "hcl": lambda s: re.match(r"^#[0-9a-f]{6}$", s),
    "ecl": lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda s: re.match(r"^[0-9]{9}$", s),
    # "cid",
}


def validate(p):
    reqd = set(fields.keys())
    passpt = " ".join(p).split()
    for field in passpt:
        f, v = field.split(":")
        if f in reqd:
            try:
                if fields[f](v):
                    reqd.remove(f)
            except Exception:
                pass
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
