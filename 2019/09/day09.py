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

intcode = Intcode(data, extend=True)
print(intcode.output)

boost = Intcode(data, inpt=2, extend=True)
print(boost.output)
