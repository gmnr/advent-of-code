#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Advent of code day 1 solution
"""

__author__ = "Guido Minieri"
__license__ = "GPL"
__version__ = "x.x.x"

# ===========================================
#           PART 1 SOLUTION
# ===========================================

# import statemets
from itertools import cycle

# load the content of the file in memory
with open("input.txt", "r") as f:
    data = f.read()

# define the infinite list
rolling_list = cycle(list(data))

for i in range(10000):
    print(next(rolling_list))
