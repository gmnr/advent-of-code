#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().rstrip()

import re
from string import ascii_lowercase as ascii


def is_valid(string):
    invalid = "iol"
    seq = any(
        [
            "".join([string[i], string[i + 1], string[i + 2]]) in ascii
            for i in range(len(string) - 2)
        ]
    )

    double = len(re.findall(r"(\w)\1", string)) >= 2

    return double and all([x not in string for x in invalid]) and seq


def increment(string):
    s = [ord(x) for x in string]
    s[-1] += 1
    for i in range(len(s)):
        if s[i] > 122:
            s[i - 1] += 1
            s[i] = s[i] - 26
    return "".join([chr(x) for x in s])


def find_pwd(data):
    while not is_valid(data):
        data = increment(data)
    return data


# pt1
res = find_pwd(data)
print(res)
# pt2
res = increment(res)
print(find_pwd(res))
