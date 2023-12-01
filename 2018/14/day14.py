#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2018
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().strip()

score = "37"
elf1 = 0
elf2 = 1

while data not in score[-7:]:
    score += str(int(score[elf1]) + int(score[elf2]))
    elf1 = (elf1 + int(score[elf1]) + 1) % len(score)
    elf2 = (elf2 + int(score[elf2]) + 1) % len(score)

print("Part 1:", score[int(data) : int(data) + 10])
print("Part 2:", score.index(data))
