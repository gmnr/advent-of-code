#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Docstring
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'



with open('input.txt', 'r') as f:
    data = f.read()


import sys; sys.path.append('..')
from intcode import Intcode

intcode = Intcode(data)
print(intcode.output)

boost = Intcode(data, inpt=2)
print(boost.output)
