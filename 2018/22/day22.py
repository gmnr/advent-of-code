#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().splitlines()

import heapq

def get_index(coord, caves, target, depth):
    x, y = coord
    if coord == (0, 0) or coord == target:
        return (depth % 20183)
    elif y == 0:
        return (((x * 16807) + depth) % 20183)
    elif x == 0:
        return (((y * 48271) + depth) % 20183)
    else:
        return (((caves[x - 1, y] * caves[x, y - 1]) + depth) % 20183)

start = 0, 0
depth = int(data[0].split()[1])
target = tuple(int(x) for x in data[1].split()[1].split(','))

# pt 1
caves = {}
for y in range(0, target[1] + 1):
    for x in range(0, target[0] + 1):
        caves[x, y] = get_index((x, y), caves, target, depth)
print(sum(map(lambda x: x % 3, caves.values())))

def risk(x, y, caves=caves, target=target, depth=depth):
    return get_index((x, y), caves, target, depth) % 3

# pt 2
for y in range(0, target[1] + 1000):
    for x in range(0, target[0] + 1000):
        caves[x, y] = get_index((x, y), caves, target, depth)
queue = [(0, 0, 0, 1)]
best = dict()

tx, ty = target
target = (tx, ty, 1)
while queue:
    minutes, x, y, cannot = heapq.heappop(queue)
    best_key = (x, y, cannot)
    if best_key in best and best[best_key] <= minutes:
        continue
    best[best_key] = minutes
    if best_key == target:
        print(minutes)
        break
    for i in range(3):
        if i != cannot and i != risk(x, y):
            heapq.heappush(queue, (minutes + 7, x, y, i))
    
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        newx = x + dx
        newy = y + dy
        if newx < 0:
            continue
        if newy < 0:
            continue
        if risk(newx, newy) == cannot:
            continue
        heapq.heappush(queue, (minutes + 1, newx, newy, cannot))
