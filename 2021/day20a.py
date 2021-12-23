#!/usr/bin/env python

from itertools import chain
import sys

f = sys.stdin

algo = f.readline().strip()
f.readline()
image = []
for r in map(str.strip, f):
    image.append(list(r))


def extendimage(i, default):
    # new pixels are defined by one original pixel in each direction
    # so we need to extend the image-space by two in each direction
    # for all affected pixels to be included
    newi = [[default, default] + row[:] + [default, default] for row in i]
    width = len(newi[0])
    newi = (
        [[default] * width]
        + [[default] * width]
        + newi
        + [[default] * width]
        + [[default] * width]
    )
    return newi


def getblock(i, x, y, default):
    def getsquare(ax, ay):
        if ax < 0 or ax >= len(i[0]):
            return default
        if ay < 0 or ay >= len(i):
            return default
        return i[ay][ax]

    block = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            block.append(getsquare(x + dx, y + dy))
    return block
    # return i[y - 1][x - 1 : x + 2] + i[y][x - 1 : x + 2] + i[y + 1][x - 1 : x + 2]


def genpixel(block):
    byte = "".join(block).replace(".", "0").replace("#", "1")
    return algo[int(byte, base=2)]


def enhance(i, default):
    newi = [[default] * len(i[0]) for x in i]
    for y in range(0, len(i)):
        for x in range(0, len(i[0])):
            block = getblock(i, x, y, default)
            newpixel = genpixel(block)
            newi[y][x] = newpixel
    return newi


iterations = 2
for i in range(iterations):
    # Since the field is infinite, the areas more than two steps away from
    # our image field will all be empty at first, but after every odd-numbered
    # step will be populated with whatever the first (index 0b000000000)
    # character of the algorithm is.
    default = "."
    if (i % 2) == 1:
        default = algo[0]
    image = extendimage(image, default=default)
    image = enhance(image, default=default)

print(len(list(filter(lambda x: x == "#", chain.from_iterable(image)))))
