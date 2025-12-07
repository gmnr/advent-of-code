#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day2 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


import sys

sys.path.append("..")
from intcode import Intcode

# get data
with open("input.txt", "r") as f:
    data = f.read()

data = list(data)
data[2] = "12"
data[4] = "2"
data = "".join(data)

intcode = Intcode(data)
print(intcode.arr[0])

target = 19690720
print(intcode.findTarget(target))
