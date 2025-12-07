#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 02 2020
"""

__author__ = "gmnr"
__license__ = "GPL"

with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]


def validate_pt1(rule, pwd):
    amount, target = rule.split(" ")
    target = str(target)
    min_a, max_a = amount.split("-")
    min_a = int(min_a)
    max_a = int(max_a)
    pwd_a = pwd.count(target)
    return pwd_a in range(min_a, max_a + 1)


# solve part 1
count_pt1 = 0
for item in data:
    if validate_pt1(*item.split(": ")):
        count_pt1 += 1
print(count_pt1)


def validate_pt2(rule, pwd):
    amount, target = rule.split(" ")
    target = str(target)
    min_a, max_a = amount.split("-")
    min_a = int(min_a) - 1
    max_a = int(max_a) - 1
    pos = [pwd[min_a], pwd[max_a]]
    return target in pos and not "".join(pos) == target * 2


# solve part 2
count_pt2 = 0
for item in data:
    if validate_pt2(*item.split(": ")):
        count_pt2 += 1
print(count_pt2)
