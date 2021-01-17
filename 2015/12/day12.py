#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day12 2015
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read()

import re
from json import loads

# pt1
digits = r'-\d+|\d+'
nums = [int(x) for x in re.findall(digits, data)]
print(sum(nums))
# pt2
new_data = loads(data)

def red_exclude(data):
    if type(data) == int:
        return data
    if type(data) == list:
        return sum(map(red_exclude, data))
    if type(data) == dict:
        vals = data.values()
        if 'red' in vals:
            return 0
        return sum(map(red_exclude, vals))
    else:
        return 0

print(red_exclude(new_data))
