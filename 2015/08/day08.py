#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day08 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()


def encode(string):
    encoded = string.replace("\\", r"\\").replace('"', '\\"')
    return '"' + encoded + '"'


enc = []
lit = []
mem = []
for i in data:
    e = len(encode(i))
    l = len(i)
    m = len(eval(i))
    enc.append(e)
    lit.append(l)
    mem.append(m)

# pt1
print(sum(lit) - sum(mem))
# pt2
print(sum(enc) - sum(lit))
