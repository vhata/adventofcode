#!/usr/bin/env python

import sys

LITERAL = 4

TOT_LENGTH = 7 + 15
SUB_PACKETS = 7 + 11


def get_type_name(t):
    if t == LITERAL:
        return "LIT"
    else:
        return "OP"


class Packet:
    bits = None
    _version = None
    _typeid = None
    _value = None
    _length = None
    _length_type = None
    _total_length = None
    _subpackets = None
    _version_sum = None
    abs_offset = 0

    def __init__(self, bits, abs_offset=0):
        self.bits = bits
        self.abs_offset = abs_offset

    @classmethod
    def from_hex(cls, hex_p):
        bits = []
        for c in list(hex_p):
            bits.extend(list(list("{0:04b}".format(int(c, base=16)))))
        p = cls(bits)
        p.hex = hex_p
        return p

    def __repr__(self) -> str:
        return (
            f"({get_type_name(self.typeid)}v{self.version}@{self.abs_offset}) "
            f"{self.value} <len:{self.length} tlen:{self.total_length} sum:{self.version_sum}> "
            f"-> [{len(self.subpackets)}]"
        )

    @property
    def version(self):
        if not self._version:
            self._version = int("".join(self.bits[:3]), base=2)
        return self._version

    @property
    def typeid(self):
        if not self._typeid:
            self._typeid = int("".join(self.bits[3:6]), base=2)
        return self._typeid

    @property
    def value(self):
        if not self._value:
            if self.typeid == LITERAL:
                plen = 6  # version + type
                val = ""
                while self.bits[plen] != "0":
                    val = val + "".join(self.bits[plen + 1 : plen + 5])
                    plen = plen + 5
                val = val + "".join(self.bits[plen + 1 : plen + 5])
                end = plen + 5
                self._value = int(val, base=2)
                self._length = end
                self._length_type = LITERAL
                self._payload = self.bits[plen:end]
            else:
                self._value = None
        return self._value

    @property
    def length(self):
        if not self._length:
            if self.typeid == LITERAL:
                # access value 'property' to trigger population
                # of internal variables
                _ = self.value
            else:
                length_type_id = self.bits[6]
                if length_type_id == "0":  # total length
                    self._length = int("".join(self.bits[7 : 7 + 15]), base=2)
                    self._length_type = TOT_LENGTH
                    self._payload = self.bits[
                        7 + TOT_LENGTH : 7 + TOT_LENGTH + self.length
                    ]
                else:  # number of sub-packets
                    self._length = int("".join(self.bits[7 : 7 + 11]), base=2)
                    self._length_type = SUB_PACKETS
                    self._payload = self.bits[7 + self.length_type :]
        return self._length

    @property
    def length_type(self):
        if not self._length_type:
            # access length 'property' to trigger population
            # of internal variables
            _ = self.length
        return self._length_type

    @property
    def payload(self):
        if not self._payload:
            # access length 'property' to trigger population
            # of internal variables
            _ = self.length
        return self._payload

    @property
    def total_length(self):
        if not self._total_length:
            if self.typeid == LITERAL:
                self._total_length = self.length
            elif self.length_type == TOT_LENGTH:
                self._total_length = TOT_LENGTH + self.length
            else:
                self._total_length = SUB_PACKETS + sum(
                    p.total_length for p in self.subpackets
                )
        return self._total_length

    @property
    def subpackets(self):
        if not self._subpackets:
            if self.typeid == LITERAL:
                self._subpackets = []
            else:
                subs = []
                pos = self.length_type
                cur = pos
                dest = self.length
                if self.length_type == SUB_PACKETS:
                    cur = 0
                else:
                    dest = TOT_LENGTH + self.length
                while cur < dest:
                    p = Packet(list(self.bits[pos:]), abs_offset=self.abs_offset + pos)
                    pos = pos + p.total_length
                    if self.length_type == SUB_PACKETS:
                        cur = cur + 1
                    else:
                        cur = pos
                    subs.append(p)
                self._subpackets = subs
        return self._subpackets

    @property
    def version_sum(self):
        if not self._version_sum:
            v = self.version
            for s in self.subpackets:
                v = v + s.version_sum
            self._version_sum = v
        return self._version_sum

    def tree(self, indent=0):
        ind = "  " * indent
        tree = (
            f"{ind}({get_type_name(self.typeid)}v{self.version}@{self.abs_offset}) "
            f"{self.value} <len:{self.length} tlen:{self.total_length} sum:{self.version_sum}> "
            f"-> [{len(self.subpackets)}]\n"
        )
        for sp in self.subpackets:
            tree = tree + sp.tree(indent + 1)
        return tree


for r in map(str.strip, sys.stdin):
    print(Packet.from_hex(r).version_sum)
