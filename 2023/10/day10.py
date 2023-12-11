#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day10 2023
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


import helper.advent as aoc
from collections import deque

data = aoc.read_input()


def connect_pipes(origin, dest, sign):
    pipes = {
        "|": [(1, 0), (-1, 0)],
        "-": [(0, 1), (0, -1)],
        "L": [(0, 1), (-1, 0)],
        "J": [(0, -1), (-1, 0)],
        "7": [(1, 0), (0, -1)],
        "F": [(1, 0), (0, 1)],
        "S": [(1, 0), (0, 1), (-1, 0), (0, -1)],
    }

    if sign == ".":
        return False

    poss = pipes[sign]
    ro, co = origin
    rd, cd = dest

    res = []

    for p in poss:
        rp, cp = p
        rr = ro + rp
        cr = co + cp

        if rd == rr and cd == cr:
            res.append((rd, cd))

    if res:
        return True

    return False


# pt 1
coords = {}
for r, line in enumerate(data):
    for c, char in enumerate(line):
        coords[(r, c)] = char

start = [k for k, v in coords.items() if v == "S"][0]
to_visit = deque([start])
loop = set([start])

while to_visit:
    c = to_visit.popleft()
    for n in aoc.gen_coordinates(c):
        if (
            n not in loop
            and n in coords
            and connect_pipes(c, n, coords[c])
            and connect_pipes(n, c, coords[n])
        ):
            to_visit.append(n)
            loop.add(n)
print(int(len(loop) / 2))

# pt 2
cnt = r = 0
l = len(data)
while r < l:
    c = 0
    inside = False
    next = None
    while c < len(data[r]):
        if (r, c) in loop:
            if coords[(r, c)] in ("|", next):
                next = None
                inside = not inside
            elif coords[(r, c)] == "L":
                next = "7"
            elif coords[(r, c)] == "F":
                next = "J"
        else:
            cnt += inside
        c += 1
    r += 1
print(cnt)
