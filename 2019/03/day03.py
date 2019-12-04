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
    """Covert the instructions into an array of coordinates"""

    arr = list()  # initialize the list
    ref = [0, 0]  # define the center

    for inst in pipe:
        if inst[0] == 'U':
            ref[1] += int(inst[1:])
        elif inst[0] == 'D':
            ref[1] -= int(inst[1:])
        elif inst[0] == 'R':
            ref[0] += int(inst[1:])
        elif inst[0] == 'L':
            ref[0] -= int(inst[1:])

        stored = list(ref)  # copy the value before appending to solve reference issues
        arr.append(stored)  # append the converted coordinate to the array

    return arr

parsed_pipe1 = parse_instructions(pipe1)
parsed_pipe2 = parse_instructions(pipe2)
