#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 05 2015
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()

import re


def is_nice(string):
    vow = r"[aieou]"
    double = r"(.)\1"
    naughty = r"ab|cd|pq|xy"
    return (
        len(re.findall(vow, string)) >= 3
        and len(re.findall(double, string)) > 0
        and len(re.findall(naughty, string)) == 0
    )


def better_is_nice(string):
    double = r"(.{2}).*\1"
    repetition = r"(.).\1"
    return (
        len(re.findall(double, string)) > 0 and len(re.findall(repetition, string)) > 0
    )


# pt 1
print(sum(is_nice(x) for x in data))
# pt 2
print(sum(better_is_nice(x) for x in data))
