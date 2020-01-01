#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day2 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import sys; sys.path.append('..')
from intcode import Intcode

# get data
with open('input.txt', 'r') as f:
    data = f.read()


solution = Intcode(data)
target = 19690720

# Print the solutions
print(f"The solution for Part 1 is {solution.op_parser()}")
print(f"The solution for Part 2 is {solution.find_target(target)}")
