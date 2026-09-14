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

new_data = list(data)
new_data[2] = "12"
new_data[4] = "2"
new_data = "".join(new_data)

intcode = Intcode(new_data)
print(intcode.mem[0])

target = 19690720
for noun in range(100):
    for verb in range(100):
        try_data = data.split(",")
        try_data[1] = str(noun)
        try_data[2] = str(verb)
        intcode = Intcode(",".join(try_data))
        if intcode.mem[0] == target:
            print(100 * noun + verb)
