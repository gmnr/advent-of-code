#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day04 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import Counter, defaultdict

data = aoc.read_input()

# pt 1 & 2
count = 0
card_counter = defaultdict(int)
for n, x in enumerate(data, 1):
    card_counter[str(n)] += 1

    c, numbers = x.split("|")
    _, winners = c.split(":")
    cnt = Counter(aoc.ints(numbers) + aoc.ints(winners))
    wins = sum(True for _, k in cnt.items() if k > 1)

    for _ in range(card_counter[str(n)]):
        for x in range(1, wins + 1):
            card_counter[str(n + x)] += 1

    if wins == 0:
        continue
    elif wins == 1:
        count += 1
    else:
        count += 2 ** (wins - 1)
print(count)
print(sum(card_counter.values()))
