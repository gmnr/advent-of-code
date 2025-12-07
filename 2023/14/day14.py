#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day14 2023
"""

__author__ = "gmnr"
__license__ = "GPL"

import helper.advent as aoc

data = aoc.read_input()


def move(movable, immote):
    new = immote.copy()
    for r, c in sorted(movable):
        r -= 1
        while r >= 0 and (r, c) not in new:
            r -= 1
        new.add((r + 1, c))

    return new - immote


movable = set()
immote = set()
for r, row in enumerate(data):
    for c, char in enumerate(row):
        if char == "O":
            movable.add((r, c))
        elif char == "#":
            immote.add((r, c))
        else:
            continue

# pt 1
new_movable = move(movable, immote)
cnt = 0
for r, _ in new_movable:
    cnt += len(data) - r
print(cnt)


# pt 2
def rotate_set(coords, l):
    return set((c, l - r - 1) for r, c in coords)


def spin_cycle(movable, immote, h, w):
    seen = {frozenset(movable): 0}

    for i in range(1, 1_000_000_000 + 1):
        movable = rotate_set(move(movable, immote), h)
        immote = rotate_set(immote, h)
        movable = rotate_set(move(movable, immote), w)
        immote = rotate_set(immote, w)
        movable = rotate_set(move(movable, immote), h)
        immote = rotate_set(immote, h)
        movable = rotate_set(move(movable, immote), w)
        immote = rotate_set(immote, w)

        key = frozenset(movable)
        if key in seen:
            break

        seen[key] = i

    cycle_len = i - seen[key]
    remaining = 1_000_000_000 - seen[key]
    final = remaining % cycle_len + seen[key]

    for key, i in seen.items():
        if i == final:
            break

    return sum(map(lambda x: h - x[0], key))


print(spin_cycle(movable, immote, len(data), len(data[0])))
