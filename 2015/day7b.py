#!/usr/bin/env python

from functools import partial
import re
import sys

wires = dict()

ops = {
    "and": lambda a, b: a & b,
    "or": lambda a, b: a | b,
    "lshift": lambda a, b: a << b,
    "rshift": lambda a, b: a >> b,
    "not": lambda a, b: a ^ 0xFFFF,
    "lit": lambda a, b: a,
}

retcache = {}


def makewire(op, a=None, b=None, name=None):
    op = op.lower()

    def wire():
        key = name
        if key in retcache:
            return retcache[key]
        l, r = a, b
        if callable(a):
            l = a()
        elif isinstance(a, str):
            try:
                l = int(a)
            except ValueError:
                l = wires[a]()
        if callable(b):
            r = b()
        elif isinstance(b, str):
            try:
                r = int(b)
            except ValueError:
                r = wires[b]()
        ret = ops[op](l, r)
        retcache[key] = ret
        return ret

    return wire


for r in map(str.strip, sys.stdin):
    m = re.match(r"^(\S+) (\S+) (\S+) -> (\S+)", r)
    if m:
        wires[m.group(4)] = makewire(m.group(2), m.group(1), m.group(3), m.group(4))
    else:
        m = re.match(r"^(\S+) (\S+) -> (\S+)", r)
        if m:
            wires[m.group(3)] = makewire(m.group(1), m.group(2), None, m.group(3))
        else:
            m = re.match(r"^(\S+) -> (\S+)", r)
            if m:
                wires[m.group(2)] = makewire("lit", m.group(1), None, m.group(2))

asig = wires["a"]()
retcache = {}
wires["b"] = makewire("lit", f"{asig}", None, "b")
print(wires["a"]())
