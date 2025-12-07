#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2018
"""

__author__ = "gmnr"
__license__ = "GPL"

from collections import defaultdict as dd, deque, Counter
from time import sleep

with open("input.txt", "r") as f:
    data = f.read().splitlines()


class Cart:
    def __init__(self, _id, x, y, face):
        self._id = _id
        self.x = x
        self.y = y
        self.face = face
        self.dir = deque(["L", "S", "R"])

    def update_coord(self, new_coord):
        self.x, self.y = new_coord

    def __repr__(self):
        return f"({self.x},{self.y})"


def parse(data):
    tracks = dd()
    carts_pos = []
    cart_id = 1
    for y in range(len(data)):
        for x in range(len(data[y])):
            fig = data[y][x]
            if fig != " ":
                tracks[(x, y)] = fig
                if fig in "^v<>":
                    carts_pos.append(Cart(cart_id, x, y, fig))
                    cart_id += 1
                    if fig in "<>":
                        tracks[(x, y)] = "-"
                    elif fig in "v^":
                        tracks[(x, y)] = "|"
    return carts_pos, tracks


def draw(carts, tracks):
    track_pos = tracks.keys()
    max_x = max(track_pos, key=lambda x: x[0])[0]
    max_y = max(track_pos, key=lambda y: y[1])[1]
    matrix = [[" " for x in range(max_x + 1)] for y in range(max_y + 1)]
    for t_pos in track_pos:
        x, y = t_pos
        matrix[y][x] = tracks[t_pos]
    carts_dict = {(c.x, c.y): c.face for c in carts}
    cart_pos = carts_dict.keys()
    for c_pos in cart_pos:
        x, y = c_pos
        matrix[y][x] = carts_dict[c_pos]
    print("\n".join(["".join(x) for x in matrix]))


def rotate(face, d):
    lookup = {
        "vL": ">",
        "vS": "v",
        "vR": "<",
        ">L": "^",
        ">S": ">",
        ">R": "v",
        "^L": "<",
        "^S": "^",
        "^R": ">",
        "<L": "v",
        "<S": "<",
        "<R": "^",
    }
    lookup_val = face + d
    return lookup[lookup_val]


def turn(face, corner):
    lookup = {
        ">/": "^",
        ">\\": "v",
        "</": "v",
        "<\\": "^",
        "^/": ">",
        "^\\": "<",
        "v/": "<",
        "v\\": ">",
    }
    lookup_val = face + corner
    return lookup[lookup_val]


def move(cart, tracks):
    old_coords = (cart.x, cart.y)

    if cart.face == ">":
        new_x, new_y = cart.x + 1, cart.y
    elif cart.face == "<":
        new_x, new_y = cart.x - 1, cart.y
    elif cart.face == "^":
        new_x, new_y = cart.x, cart.y - 1
    else:
        new_x, new_y = cart.x, cart.y + 1

    new_coord = (new_x, new_y)
    rail = tracks[new_coord]
    cart.update_coord(new_coord)

    if rail in "/\\":
        cart.face = turn(cart.face, rail)
    elif rail == "+":
        d = cart.dir[0]
        cart.face = rotate(cart.face, d)
        cart.dir.rotate(-1)
    return cart


def collision(cart, moved_carts, referenced_carts):
    other_carts = [
        c for c in referenced_carts if c._id not in [x._id for x in moved_carts]
    ]
    moved_carts = [c for c in moved_carts if c._id != cart._id]
    possible = moved_carts + other_carts
    coord_possible = [(c.x, c.y) for c in possible]
    if (cart.x, cart.y) in coord_possible:
        print(cart)
        return [c._id for c in referenced_carts if (c.x, c.y) == (cart.x, cart.y)]
    return False


def tick(carts, tracks):
    new_carts = []
    collisions = []
    carts = sorted(carts, key=lambda cart: (cart.y, cart.x))
    old_carts = carts.copy()
    for cart in carts:
        cart = move(cart, tracks)
        new_carts.append(cart)
        collisions.append(collision(cart, new_carts, old_carts))
    collided = [x for x in collisions if bool(x)]
    collided = [i for sub in collided for i in sub]
    if collided:
        new_carts = [c for c in new_carts if c._id not in collided]
    return new_carts


carts, tracks = parse(data)
while len(carts) > 1:
    carts = tick(carts, tracks)
print(carts[0])
