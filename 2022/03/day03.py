#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day03 2022
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from string import ascii_lowercase as lower, ascii_uppercase as upper

data = aoc.read_input()

score = " " + lower + upper


def find_error(rucksack):
    l = int(len(rucksack) / 2)
    left, right = rucksack[:l], rucksack[l:]
    return set(left).intersection(set(right))


def find_badge(group):
    one, two, three = group
    return set(one).intersection(set(two).intersection(set(three)))


# pt 1
print(sum(score.find("".join(find_error(x))) for x in data))

# pt 2
groups = [data[x : x + 3] for x in range(0, len(data), 3)]
print(sum(score.find("".join(find_badge(x))) for x in groups))
