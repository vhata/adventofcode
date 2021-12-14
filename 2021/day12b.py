#!/usr/bin/env python

from enum import Enum
from typing import List
import sys


class Size(Enum):
    SMALL = 0
    LARGE = 1
    TERM = 2


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
            start = Cave(cave, Size.TERM)
            caves[cave] = start
    elif cave == "end":
        if not end:
            end = Cave(cave, Size.TERM)
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


def cango(route, cave):
    if cave.name == "start":
        return False
    visited_small = [c for c in route if caves[c].size == Size.SMALL]
    if (
        cave.size == Size.SMALL
        and cave.name in route
        and len(set(visited_small)) < len(visited_small)
    ):
        return False
    return True


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
            if cango(c_route, poss_cave):
                poss.append(poss_cave.name)
        for p in poss:
            routes.append(c_route + [p])

print(len(f_routes))
