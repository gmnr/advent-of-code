#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 06 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read()[:-1].split("\t")

from itertools import cycle, islice

# data = ['0', '2', '7', '0']
banks = [int(x) for x in data]

cycles = 0
seen = []
while True:
    amt = max(banks)
    start_idx = banks.index(amt)
    banks[start_idx] = 0
    iter_banks = islice(cycle(range(len(banks))), start_idx + 1, None)
    for i in range(amt):
        banks[next(iter_banks)] += 1

    bank_status = "".join([str(x) for x in banks])
    cycles += 1
    if banks in seen:
        part2 = banks
        break
    seen.append(list(banks))

# pt 1
print(cycles)
# pt 2
print(len(seen) - seen.index(part2))
