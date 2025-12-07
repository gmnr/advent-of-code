#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day24 2015
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = [int(x) for x in f.read().splitlines()]

from itertools import combinations
from functools import reduce


def combs(lst, n):
    return (c for k in range(1, n + 1) for c in combinations(lst, k))


def best_match(lst, target, n=5):
    return min(combs(lst, n), key=lambda c: (abs(target - sum(c))))


# pt 1
group_three = best_match(data, int(sum(data) / 3))
print(reduce(lambda x, y: x * y, group_three))
# pt 2
group_four = best_match(data, int(sum(data) / 4))
print(reduce(lambda x, y: x * y, group_four))
