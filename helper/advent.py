#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper library for advent-of-code
"""

__author__ = "Guido Minieri"
__license__ = "GPL"

import re


def read_input(src="input", parser=str, sep="\n") -> tuple:
    """Get input from file or variable and return a tuple based on a parser function"""
    if src == "input":
        text = open("input.txt").read()
    else:
        text = src
    return tuple(map(parser, text.rstrip().split(sep)))


def ints(text) -> tuple:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return tuple(map(int, re.findall(r"-?[0-9]+", text)))


def words(text) -> list:
    """A list of all the alphabetic words in text, ignoring non-letters."""
    return re.findall(r"[a-zA-Z]+", text)


def transpose(matrix) -> list:
    """Transpose a matrix"""
    return list(zip(*matrix))


def rotate90(matrix):
    """Rotate a list of arrays by 90 deg"""
    new = set()
    for c in range(len(matrix[0])):
        new_row = set(row[c] for row in matrix)[::-1]
        new.add(new_row)
    return new


def first(iterable, default=None):
    "Return first item in iterable, or default."
    return next(iter(iterable), default)


def gen_coordinates(coord, n=4):
    """Generate 4, 8, 9 points around the given `coord`"""
    x, y = coord
    nb = ((0, 1), (1, 0), (0, -1), (-1, 0))
    if n == 4:
        pass
    elif n == 8:
        nb = ((1, 1), (1, -1), (-1, 1), (-1, -1)) + nb
    elif n == 9:
        nb = ((1, 1), (1, -1), (-1, 1), (-1, -1), (0, 0)) + nb
    else:
        return False
    yield from ((x + dx, y + dy) for dx, dy in nb)


def manhattan_dist(a, b) -> int:
    """Calculate manhattan distance between two points"""
    ax, ay = a
    bx, by = b
    return abs(ax - bx) + abs(ay - by)
