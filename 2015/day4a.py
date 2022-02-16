#!/usr/bin/env python

from hashlib import md5
import sys

key = sys.stdin.readline().strip()

seeking = "00000"
i = 1
while True:
    if md5((key + str(i)).encode()).hexdigest().startswith(seeking):
        break
    i = i + 1

print(i)
