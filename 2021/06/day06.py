#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day06 2021
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = list(map(int, f.read().strip().split(",")))

from collections import defaultdict


def grow(data, days):
    fish = defaultdict(int)

    for f in data:
        fish[f] += 1

    for _ in range(days):
        new_fish = defaultdict(int)
        for k, v in fish.items():
            if k == 0:
                new_fish[8] += v
                new_fish[6] += v
            else:
                new_fish[k - 1] += v

            fish = new_fish
    return fish, sum(fish.values())


fish, number = grow(data, 80)
print(number)
fish, number = grow(data, 256)
print(number)
