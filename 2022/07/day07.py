#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day07 2022
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from collections import defaultdict
import helper.advent as aoc

data = aoc.read_input()

def parse(data):
    filesystem = defaultdict(list)
    path = tuple()

    for l in data:
        if l.startswith('$ cd'):
            dest = l.split()[-1]
            if dest == '..':
                path = path[:-1]
            else:
                path = path + (dest,)

        elif l.startswith('$ ls'):
            continue

        else:
            x, y = l.split()
            if x == 'dir':
                new_path = path + (y,)
                filesystem[path].append(new_path)
            else:
                filesystem[path].append(int(x))

    return filesystem

def complete(d):
    size = 0

    for f in filesystem[d]:
        if isinstance(f, int):
            size += f
        else:
            size += complete(f)

    return size

# pt 1
filesystem = parse(data)
total = 0
for f in filesystem:
    size = complete(f)
    if size <= 100_000:
        total += size
print(total)

# pt 2
space = 70_000_000
occupied = complete(('/',))
needed_to_update= 30_000_000

delta = needed_to_update - (space - occupied)
candidates = []
for f in filesystem:
    size = complete(f)
    if size >= delta:
        candidates.append(size)
print(min(candidates))
