#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day05 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


# get data
with open("input.txt", "r") as f:
    data = f.read()


import sys

sys.path.append("..")
from intcode import Intcode


# part 1
solution1 = Intcode(data, 1)
part1 = solution1.output


# part 2
solution2 = Intcode(data, 5)
part2 = solution2.output
print(f"The solution for Part 1 is {part1}\nTHe solution for Part 2 is {part2}")
