#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day17 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import helper.advent as aoc
from collections import deque
from operator import itemgetter

data = aoc.read_input()[0]

# pt 1
H_LINE = [(0, 0), (1, 0), (2, 0), (3, 0)]
CROSS  = [(0, 1), (1, 1), (1, 2), (1, 0), (2, 1)]
REV_L  = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)]
V_LINE = [(0, 0), (0, 1), (0, 2), (0, 3)]
PUNCH  = [(0, 0), (1, 0), (0, 1), (1, 1)]
rocks = [H_LINE, CROSS, REV_L, V_LINE, PUNCH]

JETS = {'>': (1, 0), '<': (-1, 0)}

def gen_rock(h, rocks, i):
    return [(x+2, y+h+1) for x, y in rocks[i]]

def move(r, dir):
    dx, dy = dir
    new_r = [(x+dx, y+dy) for x, y in r]
    x_coords = list(map(itemgetter(0), new_r))
    if min(x_coords) >= 0 and max(x_coords) <= 6:
        return new_r
    return r

def drop(rocks, turns):
    h = -1

    tower = deque([(x, -1) for x in range(7)])
    i, j = 0, 0

    for _ in range(turns):
        r = gen_rock(h+3, rocks, i)

        while True:
            move_r = move(r, JETS[data[j]])

            if any([x in tower for x in move_r]):
                r = r
            else:
                r = move_r

            down_r = move(r, (0, -1))

            if j % (len(data) - 1) == 0 and j != 0:
                j = 0
            else:
                j += 1

            if any([x in tower for x in down_r]):
                if len(tower) > 70:
                    for _ in range(len(tower) - 70):
                        tower.popleft()
                tower.extend(r)
                new_h = max(map(itemgetter(1), r))
                if new_h > h:
                    h = new_h
                break
            else:
                r = down_r

        if i % 4 == 0 and i != 0:
            i = 0
        else:
            i += 1

    return h + 1

# pt 1
height  = drop(rocks, 2022)
print(height)

# pt 2
target = 1_000_000_000_000

offset = 179
loop = 1720
base = offset + loop

n_loops = (target - offset) // loop
end = target - offset - loop * n_loops

h_start = drop(rocks, offset) - 1
h_loop = (drop(rocks, base) - 1) * n_loops - (h_start) * n_loops
h_end = drop(rocks, base + end) - drop(rocks, base) + 1
print(h_start + h_loop + h_end)
