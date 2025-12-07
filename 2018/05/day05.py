#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2018
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().strip()

from string import ascii_lowercase as al


def react(string):
    reduced = ["."]
    for c in string:
        last = reduced[-1]
        if last != c and last.lower() == c.lower():
            reduced.pop()
        else:
            reduced.append(c)
    return len(reduced[1:])


# pt 1
print(react(data))
# pt 2
print(min(react(c for c in data if c.lower() != x) for x in al))
