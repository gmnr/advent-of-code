#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Helper library for advent-of-code
"""

__author__ = "gmnr"
__license__ = "GPL"

import re
import operator
from itertools import chain
from collections import deque
from heapq import heappop, heappush


# input
def read_input(caller_scope, parser=str, sep="\n", src="input") -> tuple:
    """Get input from file or variable and return a tuple based on a parser function"""
    test = caller_scope.get("test", False)
    if test:
        return tuple(map(parser, test.rstrip().split(sep)))
    if src == "input":
        text = open("input.txt").read()
    return tuple(map(parser, text.rstrip().split(sep)))


# atomic operations
def ints(text) -> tuple:
    """A tuple of all the integers in text, ignoring non-number characters."""
    return tuple(map(int, re.findall(r"-?[0-9]+", text)))


def words(text) -> list:
    """A list of all the alphabetic words in text, ignoring non-letters."""
    return re.findall(r"[a-zA-Z]+", text)


def minmax(numbers) -> tuple:
    """A tuple of the (minimum, maximum) of numbers."""
    numbers = list(numbers)
    return min(numbers), max(numbers)


def first(iterable, default=None):
    """Return first item in iterable, or default."""
    return next(iter(iterable), default)


def add_tuples(a, b) -> tuple:
    """Sum two tuples together"""
    return mapt(operator.add, a, b)


def sub_tuples(a, b) -> tuple:
    """Subtract two tuples together"""
    return mapt(operator.sub, a, b)


flatten = chain.from_iterable


def lprint(arg) -> None:
    """Print iterable in lines"""
    print(*arg, sep="\n")


# work with matrix and grids
def tee(matrix) -> list:
    """Transpose a matrix"""
    return list(zip(*matrix))


def rotate90(matrix) -> list:
    """Rotate a list of arrays by 90 deg"""
    new = []
    for c in range(len(matrix[0])):
        new_row = [row[c] for row in matrix][::-1]
        new.append(new_row)
    return new


def to_grid(arr) -> dict:
    """Return ascii representation of grid into a dict"""
    grid = {}
    for y, line in enumerate(arr):
        for x, c in enumerate(line):
            grid[(x, y)] = c
    return grid


def neighbors(coord, n=4):
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


# path finding
def bfs_search(start, end, grid, move_fn) -> int:
    """Breadth-first search, returns the number of steps to reach goal or 0 if there is no solution"""
    frontier = deque([(start, 0)])
    explored = set([start])

    while frontier:
        current, steps = frontier.popleft()

        if current == end:
            return steps

        for next in move_fn(current):
            if next not in explored and next in grid:
                frontier.append((next, steps + 1))
                explored.add(next)
    return 0


def astar_search(start, end, move_fn, h_fn, cost_fn=lambda *_: 1):
    frontier = [(h_fn(start, end), start)]
    previous = {start: None}
    path_cost = {start: 0}

    def build_path(step):
        path = []
        curr = step
        while curr is not None:
            path.append(curr)
            curr = previous[curr]
        return path[::-1]

    while frontier:
        f, step = heappop(frontier)

        if h_fn(step, end) == 0 or step == end:
            return build_path(step)

        if f > path_cost[step] + h_fn(step, end):
            continue

        for next_step in move_fn(step):
            g = path_cost[step] + cost_fn(step, next_step)
            if next_step not in path_cost or g < path_cost[next_step]:
                path_cost[next_step] = g
                previous[next_step] = step
                heappush(frontier, (g + h_fn(next_step, end), next_step))

    return None
