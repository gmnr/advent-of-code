#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper library for advent-of-code
"""

__author__ = "Guido Minieri"
__license__ = "GPL"

import re
from heapq import heappop, heappush


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


def quantity(iterable, pred=bool) -> int:
    """Count the number of items in iterable for which pred is true."""
    return sum(1 for item in iterable if pred(item))


def transpose(matrix) -> list:
    """Transpose a matrix"""
    return list(zip(*matrix))


def rotate90(l) -> set:
    """Rotate by 90 deg"""
    new = set()
    for c in range(len(l[0])):
        new_row = set(row[c] for row in l)[::-1]
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


def astar(start, h_func, moves_func):
    """A* algorithm"""
    frontier = [(h_func(start), start)]
    previous = {start: None}
    path_cost = {start: 0}
    while frontier:
        (_, s) = heappop(frontier)
        if h_func(s) == 0:
            return Path(previous, s)
        for s2 in moves_func(s):
            new_cost = path_cost[s] + 1
            if s2 not in path_cost or new_cost < path_cost[s2]:
                heappush(frontier, (new_cost + h_func(s2), s2))
                path_cost[s2] = new_cost
                previous[s2] = s
    return dict(fail=True, front=len(frontier), prev=len(previous))


def Path(previous, s):
    return [] if (s is None) else Path(previous, previous[s]) + [s]


def lprint(arg):
    """Print iterable in lines"""
    print(*arg, sep="\n")
