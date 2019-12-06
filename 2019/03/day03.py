#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 3 of 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


# import data
with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')


pipe1 = data[0].split(',')
pipe2 = data[1].split(',')


def parse_instructions(pipe):
    """Convert the instructions into an array of coordinates"""

    arr = list()  # initialize the list
    ref = [0, 0]  # define the center

    for inst in pipe:
        for amount in range(1, int(inst[1:]) + 1):
            if inst[0] == 'U':
                ref[1] += 1
            elif inst[0] == 'D':
                ref[1] -= 1
            elif inst[0] == 'R':
                ref[0] += 1
            elif inst[0] == 'L':
                ref[0] -= 1
            arr.append(list(ref))

    return arr

# pp stands for parsed_pipe
pp1 = parse_instructions(pipe1)
pp2 = parse_instructions(pipe2)


# find the intersection between the two lists



solution = min([abs(0 - x[0]) + abs(0 - x[1]) for x in intersections])
print(solution)
