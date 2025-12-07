#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2015
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

from collections import defaultdict as dd
import re

my_sue = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse(data):
    sues = dd(dict)
    props = [
        "children",
        "cats",
        "samoyeds",
        "pomeranians",
        "akitas",
        "vizslas",
        "goldfish",
        "trees",
        "cars",
        "perfumes",
    ]

    for i, line in enumerate(data):
        sue, *rest = line.split(", ")
        sue = re.sub("Sue \d+: ", "", sue)
        rest += [sue]
        d = {k: None for k in props}
        for el in rest:
            val, amt = el.split(": ")
            d[val] = int(amt)
        sues[i] = d
    return sues


def compare_sues(d1, d2):
    return [(v1, v2) for v1, v2 in zip(d1.values(), d2.values())]


def is_sue(comp, pt2=False):
    if not pt2:
        for x in comp:
            if x[0] == None:
                continue
            else:
                if x[0] != x[1]:
                    return False
    else:
        more = [1, 7]  # indices of properties to check
        less = [3, 6]
        for i in range(len(comp)):
            if comp[i][0] == None:
                continue
            else:
                if i in more:
                    if comp[i][0] < comp[i][1]:
                        return False
                elif i in less:
                    if comp[i][0] > comp[i][1]:
                        return False
                else:
                    if comp[i][0] != comp[i][1]:
                        return False
    return True


# pt1
sues = parse(data)
compares = [compare_sues(x, my_sue) for x in sues.values()]
the_sue = [is_sue(x) for x in compares]
print(the_sue.index(True) + 1)
# pt 2
the_real_sue = [is_sue(x, True) for x in compares]
idx = [i + 1 for i in range(len(the_real_sue)) if the_real_sue[i]]
print(max(idx))
