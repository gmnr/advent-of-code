#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 4
"""

__author__ = "gmnr"
__license__ = ""


problem = [str(x) for x in range(240920, 789857 + 1)]  # convert into string

# Part 1
import re  # solve with regex


def check_ord(lst):
    """Check the ordinality of a number"""

    if list(lst) == sorted(lst):
        return True


regex1 = re.compile(r"(\d)\1")  # create the regex
filter1 = list(filter(regex1.search, problem))  # find all doubles

solution1 = list(filter(check_ord, filter1))  # apply the function to the list
print(len(solution1))


# Part 2
from collections import Counter


def find_two(dct):
    """Pass the any function to a dictionary and check if at least one value is duplicate"""

    return any(x == 2 for x in dct.values())


solution2 = list(filter(find_two, [Counter(x) for x in solution1]))
print(len(solution2))
