#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day20 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    alg, img = f.read().split("\n\n")

from collections import defaultdict
from itertools import cycle


def nb8(coord):
    x, y = coord
    return sorted(
        [
            (x + dx, y + dy)
            for dx, dy in [
                (1, 0),
                (1, -1),
                (0, -1),
                (-1, -1),
                (0, 0),
                (-1, 0),
                (-1, 1),
                (0, 1),
                (1, 1),
            ]
        ],
        key=lambda x: (x[1], x[0]),
    )


def parse(data):
    img = defaultdict(lambda: ".")
    for y, line in enumerate(data.splitlines()):
        for x, c in enumerate(line):
            img[x, y] = c
    return img


def add_layer(img):
    d_max = max(img, key=lambda x: x[0])[0]
    d_min = min(img, key=lambda x: x[0])[0]
    low, up = d_min - 2, d_max + 2
    for y in range(low, up + 1):
        for x in range(low, up + 1):
            img[x, y] = img[x, y]
    return img


def transform(img, alg, v):
    new = defaultdict(lambda: v)
    img = add_layer(img)
    for c in img:
        k = ""
        for n in nb8(c):
            if n not in img:
                k += "0"
                continue
            k += "1" if img[n] == "#" else "0"
        k = int(k, 2)
        val = alg[k]
        new[c] = val

    new = trim(new, v)
    return new


def trim(img, v):
    trimmed = defaultdict(lambda: v)
    d_max = max(img, key=lambda x: x[0])[0]
    d_min = min(img, key=lambda x: x[0])[0]
    for y in range(d_min, d_max + 1):
        for x in range(d_min, d_max + 1):
            if x == d_min or x == d_max or y == d_min or y == d_max:
                continue
            trimmed[x, y] = img[x, y]
    return trimmed


# pt 1 & 2
img = parse(img)
outer = cycle(["#", "."])
for i, val in enumerate(outer):
    img = transform(img, alg, val)
    if i == 1:
        print(len([x for x in img.values() if x == "#"]))
    if i == 49:
        print(len([x for x in img.values() if x == "#"]))
        break
