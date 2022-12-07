#!/usr/bin/env python3

import re
import sys

TOTAL = 70000000
NEEDED = 30000000


def getline():
    for r in map(str.strip, sys.stdin):
        yield r


dirs = {}


def dodir(dir):
    global dirs
    localdirs = set()
    localsize = 0
    reading_ls = False
    for cmd in getline():
        if cmd.startswith("$"):
            reading_ls = False

        if cmd.startswith("$ cd "):
            newdir = cmd[5:]
            # maybe we're done here
            if newdir == "..":
                return localsize

            # otherwise we're going in
            assert newdir in localdirs
            fullnewdir = f"{dir}/{newdir}"
            dirs[fullnewdir] = dodir(fullnewdir)
            localsize = localsize + dirs[fullnewdir]
        elif cmd.startswith("$ ls"):
            reading_ls = True
        elif re.match(r"^[0-9]", cmd):
            assert reading_ls
            size, _ = cmd.split(None, 2)
            localsize = localsize + int(size)
        elif cmd.startswith("dir "):
            assert reading_ls
            _, subdir = cmd.split(None, 2)
            assert subdir not in localdirs
            localdirs.add(subdir)
    return localsize


cmd = next(getline())
assert cmd == "$ cd /"
dirs["/"] = dodir("")

unused_space = TOTAL - dirs["/"]
still_needed = NEEDED - unused_space
print(
    next(
        dirs[dir]
        for dir in sorted(dirs, key=lambda x: dirs[x])
        if dirs[dir] > still_needed
    )
)
