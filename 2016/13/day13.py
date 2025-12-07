#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2016
"""

__author__ = "gmnr"
__license__ = "GPL"


from helper import advent as aoc

salt = aoc.read_input(parser=int)[0]
start, target = (1, 1), (31, 39)


def space(coord, salt):
    x, y = coord
    b = bin(x * x + 3 * x + 2 * x * y + y + y * y + salt)
    b = sum(int(x) for x in b[2:])
    if b % 2 == 0:
        return "."
    else:
        return "#"


def adj(coord, salt):
    for c in aoc.gen_coordinates(coord):
        cx, cy = c
        if space(c, salt) == "." and cx >= 0 and cy >= 0:
            yield c


def traverse(start, end):
    queue = [(0, start)]
    visited = set()

    while queue:
        dist, node = queue.pop(0)

        if node == end:
            return dist

        if node not in visited:
            visited.add(node)

            for n in adj(node, salt):
                if n in visited:
                    continue

                queue.append((dist + 1, n))


def count_reachable(start, limit):
    queue = [start]
    distance = {start: 0}
    while queue:
        node = queue.pop(0)
        if distance[node] < limit:
            for n in adj(node, salt):
                if n not in distance:
                    queue.append(n)
                    distance[n] = distance[node] + 1
    return len(distance)


# pt 1
print(traverse(start, target))

# pt 2
print(count_reachable(start, 50))
