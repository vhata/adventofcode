#!/usr/bin/env python

from enum import Enum
from typing import List
import sys


class Size(Enum):
    SMALL = 0
    LARGE = 1


class Cave:
    name: str
    size: Size
    routes: List[str]

    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.routes = []

    def __repr__(self):
        return f"({self.name})"


caves = {}
start, end = None, None


def make_cave(cave):
    global start, end
    if cave == "start":
        if not start:
            start = Cave(cave, Size.SMALL)
            caves[cave] = start
    elif cave == "end":
        if not end:
            end = Cave(cave, Size.SMALL)
            caves[cave] = end
    elif cave[0].islower():
        if cave not in caves:
            caves[cave] = Cave(cave, Size.SMALL)
    else:
        if cave not in caves:
            caves[cave] = Cave(cave, Size.LARGE)


for r in map(str.strip, sys.stdin):
    a, b = r.split("-")
    make_cave(a)
    make_cave(b)
    if a not in caves[b].routes:
        caves[b].routes.append(a)
    if b not in caves[a].routes:
        caves[a].routes.append(b)

routes = [["start"]]
f_routes = []

while routes:
    c_route = routes.pop()
    if c_route[-1] == "end":
        f_routes.append(c_route)
    else:
        c_cave = c_route[-1]
        poss = []
        for r in caves[c_cave].routes:
            poss_cave = caves[r]
            if poss_cave.size == Size.LARGE or r not in c_route:
                poss.append(poss_cave.name)
        for p in poss:
            routes.append(c_route + [p])

print(len(f_routes))
