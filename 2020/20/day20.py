#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 20 2020
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")[:-1]

from itertools import combinations
from operator import add, itemgetter


def parse_tiles(data):
    tiles = {}
    for tile in data:
        number, img = tile.split(":\n")
        number = int(number.split()[1])
        tiles[number] = list_to_image(img)
    return tiles


def list_to_image(img):
    return [[x for x in y] for y in img.split("\n")]


def rot90(img):
    return list(zip(*img[::-1]))


def rotations(img):
    yield img
    for _ in range(3):
        img = rot90(img)
        yield img


def poss_orientations(img):
    yield from rotations(img)
    yield from rotations(img[::-1])


def grid(coords):
    coords = {v: k for k, v in coords.items()}
    size = int(len(coords) ** 0.5)
    offx = min(map(itemgetter(0), coords)) * -1
    offy = min(map(itemgetter(1), coords)) * -1

    grid = [[None for x in range(size)] for y in range(size)]

    for c, val in coords.items():
        x, y = c
        x, y = x + offx, y + offy
        grid[y][x] = val

    return grid[::-1]


def score_corner(grid):
    size = int(len(coord) ** 0.5) - 1
    val1 = grid[0][0]
    val2 = grid[0][size]
    val3 = grid[size][0]
    val4 = grid[size][size]
    return val1 * val2 * val3 * val4


def get_edges(img):
    top = img[0]
    bottom = img[-1]
    left = ""
    right = ""
    for row in img:
        left += row[0]
        right += row[-1]
    return {0: "".join(top), 1: right, 2: "".join(bottom), 3: left}


def match_two(tile1, tile2):
    edge1 = get_edges(tile1)

    for comb in poss_orientations(tile2):
        edge2 = get_edges(comb)

        for k1, v1 in edge1.items():
            for k2, v2 in edge2.items():
                if k1 == 0 and k2 == 2:
                    if v1 == v2:
                        return k1, comb
                elif k1 == 1 and k2 == 3:
                    if v1 == v2:
                        return k1, comb
                if k1 == 2 and k2 == 0:
                    if v1 == v2:
                        return k1, comb
                if k1 == 3 and k2 == 1:
                    if v1 == v2:
                        return k1, comb
    return False


def build(tiles):
    ops = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

    ids = list(tiles.keys())
    curr = ids[0]
    curr_img = tiles[curr]

    coord = {curr: (0, 0)}
    new_tiles = {curr: curr_img}

    matched = []
    seen = set()

    while len(coord.keys()) != len(tiles.keys()):
        for main in ids:
            if main == curr or curr in seen:
                continue

            if match_two(curr_img, tiles[main]):
                d, img = match_two(curr_img, tiles[main])
                coord[main] = tuple(map(add, coord[curr], ops[d]))
                new_tiles[main] = img
                matched.append(main)

        seen.add(curr)
        curr = matched[0]
        curr_img = new_tiles[curr]
        matched.pop(0)

    return coord, new_tiles


def strip(tiles):
    return {k: [row[1:-1] for row in v[1:-1]] for k, v in tiles.items()}


def image(grid, tiles):
    image = []

    for k, v in tiles.items():
        tiles[k] = ["".join(x) for x in v]

    grid = [[tiles[x] for x in y] for y in grid]

    for l in grid:
        seg = list(zip(*l))
        for x in seg:
            y = "".join(x)
            image.append(y)

    return image[::-1]


def count_pattern(image, pattern):
    pattern_h, pattern_w = len(pattern), len(pattern[0])
    img_size = len(image)
    deltas = []

    for r, row in enumerate(pattern):
        for c, cell in enumerate(row):
            if cell == "#":
                deltas.append((r, c))

    for img in poss_orientations(image):
        n = 0
        for r in range(img_size - pattern_h):
            for c in range(img_size - pattern_w):
                if all(img[r + dr][c + dc] == "#" for dr, dc in deltas):
                    n += 1

        if n != 0:
            return n


# pt 1
tiles = parse_tiles(data)
coord, tiles = build(tiles)
grid = grid(coord)
print(score_corner(grid))
# pt 2
tiles = strip(tiles)
img = image(grid, tiles)

monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

monster_cells = sum(r.count("#") for r in monster)
water_cells = sum(r.count("#") for r in img)
n_monsters = count_pattern(img, monster)
rough = water_cells - n_monsters * monster_cells
print(rough)
