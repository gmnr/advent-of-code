#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day24 2019
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


from helper import advent

test = """....#
#..#.
#..##
..#..
#...."""

data = advent.read_input()


def parse(data):
    bugs = {}
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            bugs[x, y] = c
    return bugs


def evolve(bugs):
    new_bugs = {}
    with_bugs = {k for k, v in bugs.items() if v == "#"}
    for c, v in bugs.items():
        adj = len(set(advent.gen_coordinates(c)).intersection(with_bugs))
        if v == "#":
            if adj != 1:
                new_bugs[c] = "."
            else:
                new_bugs[c] = "#"
        else:
            if adj == 1 or adj == 2:
                new_bugs[c] = "#"
            else:
                new_bugs[c] = "."
    return new_bugs


def add_hash(bugs):
    s = ""
    for y in range(5):
        for x in range(5):
            s += bugs[x, y]
        s += "\n"
    hash = 0
    for ch in s:
        hash = (hash * 281 ^ ord(ch) * 997) & 0xFFFFFFFF
    return hash


def get_bio(bugs):
    coords = {k for k, v in bugs.items() if v == "#"}
    score = 0
    for c in coords:
        x, y = c
        score += 2 ** (5 * y + x)
    return score


# pt 1
bugs = parse(data)
refs = [add_hash(bugs)]
cnt = 0
while True:
    bugs = evolve(bugs)
    val = add_hash(bugs)
    if val not in refs:
        refs.append(val)
        cnt += 1
    else:
        print(get_bio(bugs))
        break
