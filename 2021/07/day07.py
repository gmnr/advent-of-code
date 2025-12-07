#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    crabs = list(map(int, f.read().split(",")))


def align(crabs, target):
    expenditure = 0
    for c in crabs:
        expenditure += abs(c - target)
    return expenditure


def triangular_num(n):
    return (n**2 + n) // 2


def align_incremental(crabs, target):
    expenditure = 0
    for c in crabs:
        expenditure += triangular_num(abs(c - target))
    return expenditure


def find_min(crabs, fn):
    return min([fn(crabs, x) for x in range(min(crabs), max(crabs) + 1)])


# pt 1
print(find_min(crabs, align))

# pt 2
print(find_min(crabs, align_incremental))
