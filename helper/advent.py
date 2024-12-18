#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper library for advent-of-code
"""

__author__ = "Guido Minieri"
__license__ = "GPL"

import re
import heapq


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
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def lprint(arg):
    """Print iterable in lines"""
    print(*arg, sep="\n")


def mapt(function, *sequences) -> tuple:
    """`map`, with the result as a tuple."""
    return tuple(map(function, *sequences))


def mapl(function, *sequences) -> list:
    """`map`, with the result as a list."""
    return list(map(function, *sequences))


def astar(start, end, grid, fn=manhattan_dist):
    frontier = []
    heapq.heappush(frontier, (start, 0))

    previous = {start: None}
    cost = {start: 0}

    while frontier:

        current, _ = heapq.heappop(frontier)

        if current == end:
            break

        for n in gen_coordinates(current):
            if n in grid:
                new_cost = cost[current] + 1
                if n not in cost or new_cost < cost[n]:
                    cost[n] = new_cost
                    priority = new_cost + fn(n, end)
                    heapq.heappush(frontier, (n, priority))
                    previous[n] = current

    return previous, cost


def add_tuples(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub_tuples(a, b):
    return (a[0] - b[0], a[1] - b[1])
