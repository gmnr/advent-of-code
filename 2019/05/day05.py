#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day5 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


# get data
with open('input.txt', 'r') as f:
    data = f.read().strip().split(",")


# Part 1
import sys
sys.path.append('..')


from intcode import Intcode


int_op = Intcode(data)
print(int_op)

