#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day03 2025
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

data = aoc.read_input()

# pt 1
joltage = 0
for bank in data:
    int_bank = [int(x) for x in bank]
    candidates = []
    for i, v in enumerate(int_bank):
        if i == len(int_bank) - 1:
            break
        ab = str(v)
        ab += str(max(int_bank[i + 1 :]))
        candidates.append(ab)
        continue
    candidates = [int(x) for x in candidates]
    joltage += max(candidates)
print(joltage)

# pt 2
joltage = 0
for bank in data:
    block = bank[:12]
    for i in range(12, len(bank)):
        c = bank[i]
        for i in range(12):
            tmp = block[0:i] + block[i + 1 : 12] + c
            if int(tmp) > int(block):
                block = tmp
                break
    joltage += int(block)
print(joltage)
