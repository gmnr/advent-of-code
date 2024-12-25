#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day25 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from itertools import product

data = aoc.read_input(sep="\n\n")

locks = []
keys = []
for schema in data:

    specs = schema.splitlines()
    if specs[0] == "#" * 5:
        lock = [list(row) for row in specs]
        rot_lock = aoc.rotate90(lock)

        lock = [sum(1 if x == "#" else 0 for x in row) for row in rot_lock]
        locks.append([x - 1 for x in lock])

    else:
        key = [list(row) for row in specs]
        rot_key = aoc.rotate90(key)

        key = [sum(1 if x == "#" else 0 for x in row) for row in rot_key]
        keys.append([x - 1 for x in key])


def check_overlap(lock, key):
    for i in range(len(lock)):
        if lock[i] + key[i] < 6:
            continue
        else:
            return False
    return True


tot = 0
for combo in product(locks, keys):
    if check_overlap(*combo):
        tot += 1
print(tot)
