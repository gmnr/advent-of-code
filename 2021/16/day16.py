#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().strip()

from math import prod

to_bits = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


def read_stream(data):
    s = ""
    for c in data:
        s += to_bits[c]
    return s


class Packet:
    def __init__(self, data):
        self.bits = data
        self.c = 0

    def read(self, n):
        seg = self.bits[self.c : self.c + n]
        self.c += n
        return seg

    def parse(self):
        ver = int(self.read(3), 2)
        typ = int(self.read(3), 2)
        dat = self.packet_content(typ)
        return ver, typ, dat

    def packet_content(self, typ):
        if typ == 4:
            return self.value()
        return self.operator()

    def value(self):
        val = ""
        group = self.read(5)
        while group[0] != "0":
            val += group[1:]
            group = self.read(5)
        val += group[1:]
        return int(val, 2)

    def operator(self):
        length = int(self.read(1), 2)
        if length == 1:
            return self.n_sub(self.read(11))
        return self.len_sub(self.read(15))

    def n_sub(self, n):
        n = int(n, 2)
        return [self.parse() for _ in range(n)]

    def len_sub(self, l):
        limit = self.c + int(l, 2)
        packets = []
        while self.c < limit:
            packets.append(self.parse())
        return packets


def sum_ver(p):
    ver, typ, dat = p
    if typ == 4:
        return ver
    return ver + sum(map(sum_ver, dat))


def calculate(p):
    ver, typ, dat = p

    if typ == 4:
        return dat

    val = map(calculate, dat)

    if typ == 0:
        return sum(val)
    if typ == 1:
        return prod(val)
    if typ == 2:
        return min(val)
    if typ == 3:
        return max(val)
    a, b = val
    if typ == 5:
        return int(a > b)
    if typ == 6:
        return int(a < b)
    return int(a == b)


# pt 1
data = read_stream(data)
packets = Packet(data).parse()
print(sum_ver(packets))

# pt 2
print(calculate(packets))
