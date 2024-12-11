#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2024
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import defaultdict


data = aoc.read_input(parser=aoc.ints)[0]


def blink(stones, n):
    total_stones = defaultdict(int)
    for s in stones:
        total_stones[s] += 1

    for _ in range(n):
        step_stones = defaultdict(int)

        for stone, c in total_stones.items():

            if stone == 0:
                step_stones[1] += c

            elif len(str(stone)) % 2 == 0:
                m = len(str(stone)) // 2
                step_stones[int(str(stone)[:m])] += c
                step_stones[int(str(stone)[m:])] += c
            else:
                step_stones[stone * 2024] += c
        total_stones = step_stones
    return total_stones


# pt 1
print(sum(x for x in blink(data, 25).values()))

# pt 2
print(sum(x for x in blink(data, 75).values()))
