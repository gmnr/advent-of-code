#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day11 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().splitlines()


def parse(data):
    octopuses = {}
    for y, oct in enumerate(data):
        for x, lvl in enumerate(oct):
            octopuses[x, y] = int(lvl)
    return octopuses


def nb8(coord):
    x, y = coord
    return [
        (x + dx, y + dy)
        for dx, dy in [
            (1, 0),
            (1, -1),
            (0, -1),
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, 1),
            (1, 1),
        ]
    ]


def turn(data):
    for k, v in data.items():
        data[k] += 1

    while True:
        for k, v in data.items():
            if v > 9:
                nb = nb8(k)
                for n in nb:
                    if n not in data:
                        continue
                    else:
                        data[n] += 1
                data[k] = -9999

        if all([True if x <= 9 else False for x in data.values()]):
            break

    for k, v in data.items():
        if v < 0:
            data[k] = 0

    return data


# pt 1
oct = parse(data)
flash = 0
for _ in range(100):
    oct = turn(oct)
    flash += list(oct.values()).count(0)
print(flash)

# pt 2
step = 101
while True:
    oct = turn(oct)
    count = list(oct.values()).count(0)
    if count == 100:
        break
    step += 1
print(step)
