#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day18 2016
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


from helper import advent as aoc

data = aoc.read_input()[0]
safe, trap = ".", "^"


def generate(n):
    result = [data]
    for i in range(n - 1):
        previous = safe + result[-1] + safe
        result.append(
            "".join(
                (trap if previous[i - 1] != previous[i + 1] else safe)
                for i in range(1, len(previous) - 1)
            )
        )
    return result


# pt1
res = generate(40)
print("".join(res).count("."))

# pt2
res = generate(400_000)
print("".join(res).count("."))
