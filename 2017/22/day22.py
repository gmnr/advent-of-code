#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2017
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

from collections import defaultdict as dd, deque
from operator import add
from math import sqrt

def build_coord(data):
    coord = dd(lambda: '.')
    for y in range(len(data)):
        for x in range(len(data[y])):
            coord[(x, y)] = data[y][x]
    return coord

def move(times, coords):
    dirs = {
        'u': (0, -1),
        'd': (0, 1),
        'l': (-1, 0),
        'r': (1, 0)
    }

    side = int(sqrt(len(coords.keys())))
    middle = int(side/2)
    center = (middle, middle)

    face = deque(['u', 'r', 'd', 'l'])
    infections = 0

    c = [center, 'up']
    for _ in range(times):

        if coords[c[0]] == '#':
            face.rotate(-1)
            c[1] = face[0]
            coords[c[0]] = '.'

        elif coords[c[0]] == '.':
            face.rotate(1)
            c[1] = face[0]
            coords[c[0]] = '#'
            infections += 1

        c[0] = tuple(map(add, c[0], dirs[c[1]]))

    return infections


def move_advanced(times, coords):
    dirs = {
        'u': (0, -1),
        'd': (0, 1),
        'l': (-1, 0),
        'r': (1, 0)
    }

    side = int(sqrt(len(coords.keys())))
    middle = int(side/2)
    center = (middle, middle)

    face = deque(['u', 'r', 'd', 'l'])
    infections = 0

    c = [center, 'up']
    for _ in range(times):

        if coords[c[0]] == '#':
            face.rotate(-1)
            c[1] = face[0]
            coords[c[0]] = 'F'

        elif coords[c[0]] == 'F':
            face.rotate(2)
            c[1] = face[0]
            coords[c[0]] = '.'

        elif coords[c[0]] == 'W':
            coords[c[0]] = '#'
            infections += 1

        elif coords[c[0]] == '.':
            face.rotate(1)
            c[1] = face[0]
            coords[c[0]] = 'W'

        c[0] = tuple(map(add, c[0], dirs[c[1]]))

    return infections

# pt 1
coords = build_coord(data)
print(move(10_000, coords))
# pt 2
coords = build_coord(data)
print(move_advanced(10000000, coords))
