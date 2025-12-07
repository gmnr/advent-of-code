#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 3 of 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


# import data
with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")


pipe1 = data[0].split(",")
pipe2 = data[1].split(",")


def parse_instructions(pipe):
    """Convert the instructions into an array of coordinates"""

    arr = list()  # initialize the list
    ref = [0, 0]  # define the center

    for inst in pipe:
        for amount in range(1, int(inst[1:]) + 1):
            if inst[0] == "U":
                ref[1] += 1
            elif inst[0] == "D":
                ref[1] -= 1
            elif inst[0] == "R":
                ref[0] += 1
            elif inst[0] == "L":
                ref[0] -= 1
            arr.append(list(ref))

    return arr


# pp stands for parsed_pipe
pp1 = parse_instructions(pipe1)
pp2 = parse_instructions(pipe2)


# find the intersection between the two lists
set_pp1 = set(tuple(x) for x in pp1)
set_pp2 = set(tuple(x) for x in pp2)

intersections = list(
    set(set_pp1).intersection(set_pp2)
)  # convert the two lists into sets to apply intersection

solution1 = min([abs(0 - x[0]) + abs(0 - x[1]) for x in intersections])
print(solution1)


# Part 2
pp1_distance = [pp1.index(list(x)) + 1 for x in intersections]
pp2_distance = [pp2.index(list(x)) + 1 for x in intersections]

solution2 = min([x + y for x, y in zip(pp1_distance, pp2_distance)])
print(solution2)
