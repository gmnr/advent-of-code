#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


from collections import defaultdict
from helper import advent as aoc
import math

data = aoc.read_input(locals())

reactions = {}

for line in data:
    reagents, result = line.split("=>")

    result_qnt, result_name = result.split()

    ingredients = []
    for r in reagents.split(","):
        r_qnt, r_name = r.split()
        ingredients.append((int(r_qnt), r_name))

    reactions[result_name] = (int(result_qnt), ingredients)


def smelt(fuel_qnt):
    frontier = [(fuel_qnt, "FUEL")]
    leftover = defaultdict(int)
    total_ore = 0

    while frontier:

        need_qnt, chem = frontier.pop()

        if chem == "ORE":
            total_ore += need_qnt
            continue

        if leftover[chem] >= need_qnt:
            leftover[chem] -= need_qnt
            continue

        need_qnt -= leftover[chem]
        leftover[chem] = 0

        recipe_qnt, ingredients = reactions[chem]
        multi = math.ceil(need_qnt / recipe_qnt)

        for qnt, c in ingredients:
            frontier.append((qnt * multi, c))

        leftover[chem] += multi * recipe_qnt - need_qnt

    return total_ore


# pt 1
print(smelt(1))

# pt 2
REQUIRED = 10**12
high = 2
while smelt(high) < REQUIRED:
    high *= 2
low = high // 2

while high - low > 1:
    x = (low + high) // 2
    ore = smelt(x)

    if ore > REQUIRED:
        high = x
    else:
        low = x

fuel = low
print(fuel)
