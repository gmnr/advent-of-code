#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper library for advent-of-code
"""

__author__ = "gmnr"
__license__ = "GPL"

import re
import heapq
import operator
from itertools import chain
from typing import Sequence, Any


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


def rotate90(matrix) -> list:
    """Rotate a list of arrays by 90 deg"""
    new = []
    for c in range(len(matrix[0])):
        new_row = [row[c] for row in matrix][::-1]
        new.append(new_row)
    return new


def tee(matrix: Sequence[Sequence]) -> list[tuple]:
    """The transpose of a matrix: T([(1,2,3), (4,5,6)]) == [(1,4), (2,5), (3,6)]"""
    return list(zip(*matrix))


def first(iterable, default=None) -> Any:
    """Return first item in iterable, or default."""
    return next(iter(iterable), default)


def to_grid(arr) -> dict:
    """Return ascii representation of grid into a dict"""
    grid = {}
    for y, line in enumerate(arr):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid


def gen_coordinates(coord, n=4) -> Any:
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


def T(matrix: Sequence[Sequence]) -> list[tuple]:
    """Transpose a matrix: tee([(1,2,3), (4,5,6)]) == [(1,4), (2,5), (3,6)]"""
    return list(zip(*matrix))


def manhattan_dist(a, b) -> int:
    """Calculate manhattan distance between two points"""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def euclidean_dist(a, b) -> float:
    """Euclidean (L2) distance between two points."""
    d = sum((pi - qi) ** 2 for pi, qi in zip(a, b)) ** 0.5
    return int(d) if d.is_integer() else d


def mapt(function, *sequences) -> tuple:
    """`map`, with the result as a tuple."""
    return tuple(map(function, *sequences))


def mapl(function, *sequences) -> list:
    """`map`, with the result as a list."""
    return list(map(function, *sequences))


def lprint(arg) -> None:
    """Print iterable in lines"""
    print(*arg, sep="\n")


def astar(start, end, grid, cost_fn=lambda _: 1, heuristic_fn=manhattan_dist) -> tuple:
    """Imprementation of A* algo"""
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
                new_cost = cost[current] + cost_fn(n)
                if n not in cost or new_cost < cost[n]:
                    cost[n] = new_cost
                    priority = new_cost + heuristic_fn(n, end)
                    heapq.heappush(frontier, (n, priority))
                    previous[n] = current

    return previous, cost


flatten = chain.from_iterable


def add_tuples(a, b) -> tuple:
    """Sum two tuples together"""
    return mapt(operator.add, a, b)


def sub_tuples(a, b) -> tuple:
    """Subtract two tuples together"""
    return mapt(operator.sub, a, b)
