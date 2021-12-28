#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper library for advent-of-code
Contains:

    parser;
    data structure;
    recurring functions in the challenges
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'

import re

def parse(parser=str, fname='input', sep='\n') -> tuple:
    """Parse the input data into a tuple, parser can be specified"""
    fname = f'{fname}.txt'
    text = open(fname).read()
    entries = tuple(map(parser, text.rstrip().split(sep)))
    return entries

def ints(text) -> tuple:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return tuple(map(int, re.findall(r'-?[0-9]+', text)))

def quantity(iterable, pred=bool) -> int:
    """Count the number of items in iterable for which pred is true."""
    return sum(1 for item in iterable if pred(item))

def transpose(matrix) -> list:
    return list(zip(*matrix))

def first(iterable, default=None):
    "Return first item in iterable, or default."
    return next(iter(iterable), default)

nb4 = ((0, 1), (1, 0), (0, -1), (-1, 0))               
nb8 = ((1, 1), (1, -1), (-1, 1), (-1, -1)) + nb4
