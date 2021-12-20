#!/usr/bin/env python

import string
import sys

RED = "\033[91m"
GREEN = "\033[92m"
BRIGHT = "\033[1m"
NORM = "\033[00m"

EXP_NONE = 0  # no explosion happened here
EXP_ME = 1  # this node exploded
EXP_DONE = 2  # a node exploded further down, and we're just passing the numbers back to be replaced in

SPL_NONE = 0  # no split happened here
SPL_SPLAT = 1  # we split

REPR_BASIC = 0  # display SFNums naturally
REPR_DAD = 1  # include dad count of SFNums
REPR_COL = 2  # naturally with colours
REPR_DAD_COL = 3  # include colours in dad repr


class SFNum:
    left = None
    right = None
    dad = None
    REPR = REPR_BASIC

    def __init__(self, l, r, dad=None):
        self.left = l
        self.right = r
        self.dad = dad

    def __repr__(self):
        if self.REPR == REPR_BASIC:
            return f"[{self.left},{self.right}]"
        if self.REPR == REPR_DAD:
            return f"[({self.dadcount}){self.left},{self.right}]"
        if self.REPR == REPR_COL:
            return f"{NORM}[{BRIGHT}{self.left}{NORM},{BRIGHT}{self.right}{NORM}]"
        if self.REPR == REPR_DAD_COL:
            return f"{NORM}[{RED}({self.dadcount}){NORM}{BRIGHT}{self.left}{NORM},{BRIGHT}{self.right}{NORM}]"

    def __add__(self, o):
        result = SFNum(self, o)
        self.dad = o.dad = result
        result.reduce()
        return result

    def __int__(self):
        # this is the "magnitude" of the SFNum
        return int(self.left) * 3 + int(self.right) * 2

    @property
    def dadcount(self):
        if not self.dad:
            return 0
        return self.dad.dadcount + 1

    def _add_left(self, n):
        # For bubbling the numbers around after exploding
        if isinstance(self.left, int):
            self.left = self.left + n
        else:
            self.left._add_left(n)

    def _add_right(self, n):
        # For bubbling the numbers around after exploding
        if isinstance(self.right, int):
            self.right = self.right + n
        else:
            self.right._add_right(n)

    def explode(self):
        # dadcount will never be more than 4, as it would have been previously
        # exploded
        # also, left and right will definitely be ints for the same reason
        if self.dadcount == 4:
            return self.left, self.right, EXP_ME
        # Otherwise, first, try to explode the left
        if isinstance(self.left, SFNum):
            l, r, e = self.left.explode()
            if e:  # EXP_ME or EXP_DONE
                # somewhere down the line, something exploded
                if e == EXP_ME:
                    # our immediate left exploded, replace with zero
                    self.left = 0
                if r:
                    # we still have a right-number to replace, do it
                    if isinstance(self.right, SFNum):
                        # we send it to the right, but it needs to be added to
                        # the leftmost number on that side
                        self.right._add_left(r)
                    else:
                        self.right = self.right + r
                # pass back the left, not the right, and say explosion was done
                return l, None, EXP_DONE
        # Nothing on the left exploded, try on the right
        if isinstance(self.right, SFNum):
            l, r, e = self.right.explode()
            if e:  # EXP_ME or EXP_DONE
                # something expldoed
                if e == EXP_ME:
                    # immediate right exploded, replace with zero
                    self.right = 0
                if l:
                    # replace left-number
                    if isinstance(self.left, SFNum):
                        # we send it to the left, but it needs to be added to
                        # the rightmost number on that side
                        self.left._add_right(l)
                    else:
                        self.left = self.left + l
                # pass back right, not left, and say explosion was done
                return None, r, EXP_DONE
        # nothing to see here
        return None, None, EXP_NONE

    def split(self):
        def splitnum(n):
            return SFNum(n // 2, n // 2 + (n % 2), dad=self)

        spl = SPL_NONE
        if isinstance(self.left, int):
            if self.left >= 10:
                self.left = splitnum(self.left)
                return SPL_SPLAT
        else:
            spl = self.left.split()
        if not spl:  # nothing happened to the left
            if isinstance(self.right, int):
                if self.right >= 10:
                    self.right = splitnum(self.right)
                    return SPL_SPLAT
            else:
                spl = self.right.split()
        return spl

    def reduce(self):
        changing = True
        while changing:
            _, _, e = self.explode()
            if e == EXP_NONE:  # we didn't explode, try split
                e = self.split()
                if e == SPL_NONE:  # we didn't split either, all done
                    changing = False
            # if explode or split, loop again


def parseSF(s):
    cur = 0
    left, right = None, None
    while cur < len(s):
        if s[cur] == "[":
            # begin new left sub-num
            left, l = parseSF(s[cur + 1 :])
            cur = cur + 1 + l
        elif s[cur] in string.digits:
            # grab a literal digit
            v = ""
            while s[cur] in string.digits:
                v = v + s[cur]
                cur = cur + 1
            return int(v), len(v)
        elif s[cur] == ",":
            # begin new right sub-num
            right, l = parseSF(s[cur + 1 :])
            cur = cur + 1 + l
        elif s[cur] == "]":
            # end of parsing num, add it to our tree
            num = SFNum(left, right)
            if isinstance(left, SFNum):
                left.dad = num
            if isinstance(right, SFNum):
                right.dad = num
            return num, cur + 1


tot = None
for r in map(str.strip, sys.stdin):
    num, _ = parseSF(r)
    if tot == None:
        tot = num
    else:
        tot = tot + num
print(int(tot))
