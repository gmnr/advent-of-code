#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 09 2017
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read()

import re
from collections import defaultdict as dd


def del_canc(lst):
    res = []
    skip = False
    for i in range(len(lst)):
        if skip:
            skip = False
            continue
        if lst[i] == "!":
            skip = True
            continue
        else:
            res.append(lst[i])
    return "".join(res)


def del_garbage(lst):
    match = r"<.*?>"
    res = re.split(match, lst)
    return "".join(res)


def count_groups(lst):
    count = 1
    for el in lst:
        if el == "{":
            count += count
    return count


def score(lst):
    depth = dd(int)
    card = 0
    lvl = 0
    for i in lst:
        if i == "{":
            card += 1
            depth[card] += 1
        elif i == ",":
            card -= lvl
            lvl = 0
        else:
            lvl += 1
    return sum([k * v for k, v in depth.items()])


def count_garbage(lst):
    match = r"<(.*?)>"
    clean = del_canc(lst)
    matches = "".join(re.findall(match, clean))
    return len(matches)


# pt 1
res = del_garbage(del_canc(data))
print(score(res))
# pt 2
print(count_garbage(data))
