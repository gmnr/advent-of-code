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

# pp stands for parsed pipe
pp1 = parse_instructions(pipe1)
pp2 = parse_instructions(pipe2)

intersections = list()  # initialize 
for i in range(len(pp1)):
    for j in range(len(pp2)):

        try:  # wrap into try/except to avoid "out of index" error
            if pp1[i][0] == pp1[i + 1][0]:  # check vertical
                if pp2[j][1] == pp2[j + 1][1] and pp1[i][1] in range(pp2[j][0], pp2[j + 1][0]):
                    match = [pp1[i][0], pp2[j][1]]
                    intersections.append(match)


            if pp1[i][1] == pp1[i + 1][1]:  # check horizontal
                if pp2[j][0] == pp2[j + 1][0] and pp1[i][0] in range(pp2[j][1], pp2[j + 1][1]):
                    match = [pp2[j][0], pp1[i][1]]
                    intersections.append(match)
        except IndexError:
            pass

print(len(intersections))
solution = [abs(0 - x[0]) + abs(0 - x[1]) for x in intersections]

