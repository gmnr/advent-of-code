#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day18 2018
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import Counter, defaultdict as dd


def parse(data):
    acres = {}
    for y in range(len(data)):
        for x in range(len(data[y])):
            acres[(x, y)] = data[y][x]
    return acres


def tick(acres):
    new_acres = {}

    for coord in acres:
        adjacents = adjacent(coord)
        adjacents = [acres[x] for x in adjacents if x in acres]

        if acres[coord] == "." and len([x for x in adjacents if x == "|"]) >= 3:
            new_acres[coord] = "|"
        elif acres[coord] == "|" and len([x for x in adjacents if x == "#"]) >= 3:
            new_acres[coord] = "#"
        elif acres[coord] == "#":
            if (
                acres[coord] == "#"
                and len([x for x in adjacents if x == "#"]) >= 1
                and len([x for x in adjacents if x == "|"]) >= 1
            ):
                new_acres[coord] = "#"
            else:
                new_acres[coord] = "."
        else:
            new_acres[coord] = acres[coord]
    return new_acres


def adjacent(coord):
    x, y = coord
    return (
        (x + 1, y),
        (x - 1, y),
        (x, y + 1),
        (x, y - 1),
        (x - 1, y - 1),
        (x - 1, y + 1),
        (x + 1, y - 1),
        (x + 1, y + 1),
    )


def score(acres):
    nums = Counter(acres.values())
    nums = [v for k, v in nums.items() if k != "."]
    return nums[0] * nums[1]


# pt 1
acres = parse(data)
for _ in range(10):
    acres = tick(acres)
print(score(acres))
# pt 2
new_acres = parse(data)
scores = dd(int)
while True:
    new_acres = tick(new_acres)
    scores[score(new_acres)] += 1
    if max(scores.values()) > 4:
        break

involved = len([x for x in scores.values() if x >= 3])
not_involved = len(scores.values()) - involved
target = 1000000000
cycles = target - not_involved
remainder = cycles % involved
loops = remainder + not_involved
final_acres = parse(data)
for _ in range(loops):
    final_acres = tick(final_acres)
print(score(final_acres))
