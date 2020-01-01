#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intcode Class and helper functions
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


class Intcode():


    def __init__(self, data):
        """read and format the instruction set"""
        self.data = [int(x) for x in data[:-1].strip().split(',')]

        self.data = list(self.data)  # create a new list
        self.data[1] = 12
        self.data[2] = 2


    def initialize_instrucitons(self, noun=12, verb=2):
        """Create a copy of the data"""
        self.arr = list(self.data)
        self.arr[1] = noun
        self.arr[2] = verb


    def op1(self, i):
        """execute OP1: add values of 1st and 2nd index into 3rd index"""
        self.arr[self.arr[i + 3]] = self.arr[self.arr[i + 1]] + self.arr[self.arr[i + 2]]


    def op2(self, i):
        """execute OP2: multiply values of 1st and 2nd index into 3rd index"""
        self.arr[self.arr[i + 3]] = self.arr[self.arr[i + 1]] * self.arr[self.arr[i + 2]]


    def op_parser(self, *args):
        """parse the instructions executing commands"""
        self.initialize_instrucitons(*args)

        for i in range(0, len(self.arr), 4):  # start looping
            if self.arr[i] == 1:
                self.op1(i)
            if self.arr[i] == 2:
                self.op2(i)
            if self.arr[i] == 99:  # stop parsing
                break

        return self.arr[0]


    def find_target(self, target):
        """find the noun and verb that satisfy the conditions"""

        for noun in range(100):  # start nested loop
            for verb in range(100):
                if self.op_parser(noun, verb) == target:

                    return 100 * noun + verb


    def __repr__(self):
        """Check head of file"""

        return ", ".join([str(self.data[x]) for x in range(12)])
