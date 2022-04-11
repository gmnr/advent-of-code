#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2016
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from helper import advent as aoc

instructions = aoc.read_input()

class Numpad:

    def __init__(self, pt1=True):
        self.last= '5'
        self.pt1 = pt1

    def move(self, inst):

        if self.pt1:
            moves = {
                    '1': ['1', '2', '4', '1'],
                    '2': ['2', '3', '5', '1'],
                    '3': ['3', '3', '6', '2'],
                    '4': ['1', '5', '7', '4'],
                    '5': ['2', '6', '8', '4'],
                    '6': ['3', '6', '9', '5'],
                    '7': ['4', '8', '7', '7'],
                    '8': ['5', '9', '8', '7'],
                    '9': ['6', '9', '9', '8'],
            }
        else:
            moves = {
                    '1': ['1', '1', '3', '1'],
                    '2': ['2', '3', '6', '2'],
                    '3': ['1', '4', '7', '2'],
                    '4': ['4', '4', '8', '3'],
                    '5': ['5', '6', '5', '5'],
                    '6': ['2', '7', 'A', '5'],
                    '7': ['3', '8', 'B', '6'],
                    '8': ['4', '9', 'C', '7'],
                    '9': ['9', '9', '9', '8'],
                    'A': ['6', 'B', 'A', 'A'],
                    'B': ['7', 'C', 'D', 'A'],
                    'C': ['8', 'C', 'C', 'B'],
                    'D': ['B', 'D', 'D', 'D'],
            }

        l = self.last
        next = moves[l]

        if inst == 'U':
            self.last = next[0]
        elif inst == 'R':
            self.last = next[1]
        elif inst == 'D':
            self.last = next[2]
        else:
            self.last = next[3]

# pt 1
numpad = Numpad()
res = ''
for inst in instructions:
    for i in inst:
        numpad.move(i)

    res += numpad.last
print(res)

# pt 2
numpad = Numpad(False)
res = ''
for inst in instructions:
    for i in inst:
        numpad.move(i)

    res += numpad.last
print(res)
