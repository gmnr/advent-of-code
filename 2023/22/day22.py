#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day22 2023
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc
from collections import namedtuple, defaultdict
from itertools import combinations

test = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9"""


def removable(bricks):
    stack = settle(bricks)
    support = supported_by(stack)
    unsafe = {bot for top in support for bot in support[top] if len(support[top]) == 1}
    return stack - unsafe


def settle(bricks):
    heights = defaultdict(int)
    return {drop(brick, heights) for brick in sorted(bricks, key=lambda s: s.z)}


def drop(brick, heights):
    h = max(heights[p] for p in bottom(brick))
    for p in bottom(brick):
        heights[p] = h + 1 + brick.Z - brick.z
    return brick._replace(z=h + 1, Z=h + 1 + brick.Z - brick.z)


def bottom(brick):
    return {
        (x, y) for x in range(brick.x, brick.X + 1) for y in range(brick.y, brick.Y + 1)
    }


def supported_by(stack):
    support = defaultdict(list)
    for bot, top in combinations(sorted(stack, key=lambda b: b.z), 2):
        if bot.Z + 1 == top.z and not bottom(bot).isdisjoint(bottom(top)):
            support[top].append(bot)
    return support


def settle_count(bricks):
    heights = defaultdict(int)
    return sum(
        drop(brick, heights) != brick for brick in sorted(bricks, key=lambda s: s.z)
    )


def count_falls(bricks):
    stack = settle(bricks)
    result = 0
    for brick in stack:
        stack.remove(brick)
        result += settle_count(stack)
        stack.add(brick)
    return result


data = aoc.read_input()

brick = namedtuple("brick", "x, y, z, X, Y, Z")
bricks = [brick(*aoc.ints(x)) for x in data]

# pt1
print(len(removable(bricks)))

# pt2
print(count_falls(bricks))
