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


def nop(*k):
    pass
    # print(*k)


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

    def _add_left(self, n, indent):
        # For bubbling the numbers around after exploding
        ind = "  " * indent
        nop(f"{ind}A_L: {self}")
        if isinstance(self.left, int):
            self.left = self.left + n
        else:
            self.left._add_left(n, indent + 1)
        nop(f"{ind}A_L_END: {self}")

    def _add_right(self, n, indent):
        # For bubbling the numbers around after exploding
        ind = "  " * indent
        nop(f"{ind}A_R: {self}")
        if isinstance(self.right, int):
            self.right = self.right + n
        else:
            self.right._add_right(n, indent + 1)
        nop(f"{ind}A_R_END: {self}")

    def explode(self, indent=0):
        ind = "  " * indent
        nop(f"{ind}EXPL: {self} ({self.dadcount})")
        # dadcount will never be more than 4, as it would have been previously
        # exploded
        # also, left and right will definitely be ints for the same reason
        if self.dadcount == 4:
            return self.left, self.right, EXP_ME
        # Otherwise, first, try to explode the left
        if isinstance(self.left, SFNum):
            nop(f"{ind}GO LEFT")
            l, r, e = self.left.explode(indent + 1)
            nop(f"{ind}LEFT: {l}, {r}, {e}")
            if e:  # EXP_ME or EXP_DONE
                nop(f"{ind}YES")
                # somewhere down the line, something exploded
                if e == EXP_ME:
                    # our immediate left exploded, replace with zero
                    self.left = 0
                if r:
                    # we still have a right-number to replace, do it
                    if isinstance(self.right, SFNum):
                        # we send it to the right, but it needs to be added to
                        # the leftmost number on that side
                        nop(f"{ind}ADD TO LEFT OF RIGHT")
                        self.right._add_left(r, indent + 1)
                    else:
                        self.right = self.right + r
                # pass back the left, not the right, and say explosion was done
                nop(f"{ind}DONE: {self}")
                return l, None, EXP_DONE
        # Nothing on the left exploded, try on the right
        if isinstance(self.right, SFNum):
            nop(f"{ind}GO RIGHT")
            l, r, e = self.right.explode(indent + 1)
            nop(f"{ind}RIGHT: {l}, {r}, {e}")
            if e:  # EXP_ME or EXP_DONE
                nop(f"{ind}YES")
                # something expldoed
                if e == EXP_ME:
                    # immediate right exploded, replace with zero
                    self.right = 0
                if l:
                    # replace left-number
                    if isinstance(self.left, SFNum):
                        # we send it to the left, but it needs to be added to
                        # the rightmost number on that side
                        nop(f"{ind}ADD TO RIGHT OF LEFT")
                        self.left._add_right(l, indent + 1)
                    else:
                        self.left = self.left + l
                # pass back right, not left, and say explosion was done
                nop(f"{ind}DONE: {self}")
                return None, r, EXP_DONE
        # nothing to see here
        return None, None, EXP_NONE

    def split(self, indent=0):
        def splitnum(n):
            return SFNum(n // 2, n // 2 + (n % 2), dad=self)

        ind = "  " * indent
        nop(f"{ind}SPL: {self}")
        spl = SPL_NONE
        if isinstance(self.left, int):
            if self.left >= 10:
                self.left = splitnum(self.left)
                nop(f"{ind}SPLAT: {self}")
                return SPL_SPLAT
        else:
            nop(f"{ind}SPL_L")
            spl = self.left.split(indent + 1)
            nop(f"{ind}SPL_L: {spl}")
        if not spl:  # nothing happened to the left
            if isinstance(self.right, int):
                if self.right >= 10:
                    self.right = splitnum(self.right)
                    nop(f"{ind}SPLAT: {self}")
                    return SPL_SPLAT
            else:
                nop(f"{ind}SPL_R")
                spl = self.right.split(indent + 1)
                nop(f"{ind}SPL_R: {spl}")
        return spl

    def reduce(self):
        changing = True
        while changing:
            nop(f"TRY EXP")
            _, _, e = self.explode(indent=1)
            nop(f"TRY EXP: {e}")
            if e == EXP_NONE:  # we didn't explode, try split
                nop(f"TRY SPL")
                e = self.split(indent=1)
                nop(f"TRY SPL: {e}")
                if e == SPL_NONE:  # we didn't split either, all done
                    nop("WE'RE DONE")
                    changing = False
                else:
                    nop(f"AGAIN {self}")
            else:
                nop(f"AGAIN {self}")
            # if explode or split, loop again


def parseSF(s, indent=0):
    cur = 0
    ind = "  " * indent
    nop(f"{ind}Cur: {cur}")
    left, right = None, None
    while cur < len(s):
        nop(f"{ind}S: {' '*cur}V")
        nop(f"{ind}S: {s}")
        nop(f"{ind}C: {s[cur]}")
        if s[cur] == "[":
            # begin new left sub-num
            left, l = parseSF(s[cur + 1 :], indent=indent + 1)
            cur = cur + 1 + l
        elif s[cur] in string.digits:
            # grab a literal digit
            v = ""
            while s[cur] in string.digits:
                v = v + s[cur]
                cur = cur + 1
            nop(f"{ind}VAL: {int(v)}")
            return int(v), len(v)
        elif s[cur] == ",":
            # begin new right sub-num
            right, l = parseSF(s[cur + 1 :], indent=indent + 1)
            cur = cur + 1 + l
        elif s[cur] == "]":
            # end of parsing num, add it to our tree
            num = SFNum(left, right)
            if isinstance(left, SFNum):
                left.dad = num
            if isinstance(right, SFNum):
                right.dad = num
            nop(f"{ind}VAL: {num}")
            return num, cur + 1
        nop(f"{ind}Cur: {cur}")
    nop(f"{ind}Done? Shouldn't get here")


tot = None
for r in map(str.strip, sys.stdin):
    num, _ = parseSF(r)
    if tot == None:
        tot = num
    else:
        tot = tot + num
print(int(tot))
