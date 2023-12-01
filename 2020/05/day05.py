#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 5 2020
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]


def getSeatID(r, c):
    return r * 8 + c


def parseBinary(string):
    rows = string[:7]
    cols = string[7:]

    row_range = list(range(128))
    col_range = list(range(8))

    for rw in rows:
        if rw == "F":
            row_range = row_range[: int(len(row_range) / 2)]
        else:
            row_range = row_range[int(len(row_range) / 2) :]
    row = row_range[0]

    for cl in cols:
        if cl == "L":
            col_range = col_range[: int(len(col_range) / 2)]
        else:
            col_range = col_range[int(len(col_range) / 2) :]

    col = col_range[0]
    return (row, col)


# part 1
seatIDs = [getSeatID(*parseBinary(x)) for x in data]
print(max(seatIDs))

# part 2
sortID = sorted(seatIDs)
compare = list(range(min(sortID), max(sortID)))
ticket = [x for x in compare if x not in sortID]
print(ticket[0])
