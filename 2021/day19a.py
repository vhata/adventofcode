#!/usr/bin/env python

# Some of my "Point" class implementation and rotation logic was borrowed from
# Reddit user Multipl, and the "distances"/"common" idea was borrowed from
# Reddit user legija_sira.
# I started implementing something similar to them, got confused, tried to install
# and use numpy, and then scipy, then entered a world of pain, and eventually
# found their code which got me to here

from itertools import permutations, product, combinations
import math
import re
import sys


class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __neg__(self):
        return Point(-self.x, -self.y, -self.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __hash__(self):
        return hash(str(self))

    def manhattan_dist(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)


def rotategrid(m, rotation, signs):
    newpoints = []
    for point in m:
        axes = {"x": point.x, "y": point.y, "z": point.z}
        newpoints.append(
            Point(
                axes[rotation[0]] * signs[0],
                axes[rotation[1]] * signs[1],
                axes[rotation[2]] * signs[2],
            )
        )
    return newpoints


def movegrid(m, offset=None):
    if offset:
        ox, oy, oz = offset.x, offset.y, offset.z
    else:
        ox = min(c.x for c in m)
        oy = min(c.y for c in m)
        oz = min(c.z for c in m)
    newm = []
    for p in m:
        newm.append(Point(p.x - ox, p.y - oy, p.z - oz))
    return newm


def getmin(m):
    return Point(min(c.x for c in m), min(c.y for c in m), min(c.z for c in m))


class Scanner:
    def __init__(self, points):
        self.points = points
        self.location = None
        self.offset = []
        self.signs = []
        self.rotation = []
        self.getdistances()

    def __repr__(self):
        return f"{self.points}"

    def getdistances(self):
        self.distances = []
        for i in range(len(self.points)):
            p1 = self.points[i]
            distances = []

            for j in range(len(self.points)):
                if i == j:
                    continue
                p2 = self.points[j]
                dist = math.sqrt(
                    (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2 + (p2.z - p1.z) ** 2
                )
                distances.append(dist)

            distances.sort()
            self.distances.append(distances)

    def findcommon(self, other):
        common = {}
        for i in range(len(self.distances)):
            for j in range(len(other.distances)):
                c = 0
                if i in common:
                    break
                for k in range(12):
                    if self.distances[i][k] == other.distances[j][k]:
                        c += 1
                if c > 1:
                    common[i] = j
        return common

    def _getcommons(self, other):
        common = self.findcommon(other)
        mypoints = [self.points[i] for i in common.keys()]
        otherpoints = [other.points[i] for i in common.values()]
        return mypoints, otherpoints

    def align(self, other):
        mypoints, otherpoints = self._getcommons(other)
        if len(mypoints) != 12:
            return False
        centeredmy = movegrid(mypoints)
        for rotation in permutations(["x", "y", "z"]):
            for signs in product([-1, 1], repeat=3):
                newpoints = rotategrid(otherpoints, rotation, signs)
                centerednew = movegrid(newpoints)

                if set(centerednew) == set(centeredmy):
                    # build a stack of operations to get from "other" to Scanner Zero
                    other.offset = self.offset[:]
                    other.offset.append(getmin(newpoints) - getmin(mypoints))
                    other.signs = self.signs[:]
                    other.signs.append(signs)
                    other.rotation = self.rotation[:]
                    other.rotation.append(rotation)
                    return True
        return False

    def normalize(self):
        res = self.points
        for i in range(len(self.rotation) - 1, -1, -1):
            res = rotategrid(res, self.rotation[i], self.signs[i])
            res = movegrid(res, self.offset[i])
        return res


scanners = []
curscanner = None
points = []

for r in map(str.strip, sys.stdin):
    if not r:
        scanners.append(Scanner(points))
        points = []
        curscanner = None
    else:
        m = re.match(r"^--- scanner (\d+) ---", r)
        if m:
            curscanner = m.group(1)
        else:
            points.append(Point(*list(map(int, r.split(",")))))
scanners.append(Scanner(points))


matched = [scanners[0]]
to_match = scanners[1:]
while to_match:
    attempt = to_match.pop(0)

    found = False
    for m in matched:
        if m.align(attempt):
            found = True
            matched.append(attempt)
            break
    if not found:
        to_match.append(attempt)

beacons = []
for scanner in matched:
    beacons.extend(scanner.normalize())

print(len(set(beacons)))
