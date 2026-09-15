#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day09 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read()


import sys

sys.path.append("..")
from intcode import Intcode

# pt 1
process = Intcode(data).run(1)
for val in process:
    print(val)

# pt 2
process = Intcode(data).run(2)
for val in process:
    print(val)
