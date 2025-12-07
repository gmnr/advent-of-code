#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day19 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
import functools

patterns, designs = aoc.read_input(sep="\n\n")
patterns = frozenset(patterns.split(", "))
designs = designs.splitlines()


@functools.cache
def is_valid(design, patterns):
    if design == "":
        return True

    for p in patterns:
        if design.startswith(p):
            if is_valid(design[len(p) :], patterns):
                return True

    return False


@functools.cache
def arrangement_options(design, patterns):
    if design == "":
        return 1

    total = 0
    for p in patterns:
        if design.startswith(p):
            total += arrangement_options(design[len(p) :], patterns)

    return total


# pt 1
print(sum(is_valid(d, patterns) for d in designs))

# pt 2
print(sum(arrangement_options(d, patterns) for d in designs))
