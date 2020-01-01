#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intcode Class and helper functions
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


class Intcode():

    def __init__(self, data):
        self.data = [int(x) for x in data[:-1].strip().split(',')]


    def day2(self, noun=12, verb=2):
        """wrap the opcode routine into a function"""

        self.arr = list(self.data)
        self.arr[1] = noun
        self.arr[2] = verb

        for j in range(0, len(self.arr), 4):
            if self.arr[j] == 1:
                self.arr[self.arr[j + 3]] = self.arr[self.arr[j + 1]] + self.arr[self.arr[j + 2]]
            if self.arr[j] == 2:
                self.arr[self.arr[j + 3]] = self.arr[self.arr[j + 1]] * self.arr[self.arr[j + 2]]
            if self.arr[j] == 99:
                break

        return self.arr[0]

    def find_target(self, target):
        """find the noun and verb that satisfy the conditions"""

        self.target = target

        for noun in range(100):
            for verb in range(100):
                if self.day2(noun, verb) == self.target:
                    return 100 * noun + verb
             


    def __repr__(self):
        """Check head of file"""

        return ", ".join([str(self.data[x]) for x in range(12)])
