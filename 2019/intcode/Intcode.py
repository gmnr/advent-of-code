#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intcode Class and helper functions
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


class Intcode():


    def __init__(self, data, inpt=1):
        """read and format the instruction set"""
        self.data = [int(x) for x in data[:-1].strip().split(',')]

        self.data = list(self.data)  # create a new list
        self.inpt = inpt  # defaults to 1
        self.diagnostic_code = []


    def initialize_instrucitons(self, noun=None, verb=None):
        """Create a copy of the data, initialize noun/verb and c"""
        self.arr = list(self.data)

        if noun != None and verb != None:
            self.arr[1] = noun
            self.arr[2] = verb
        self.c = 0  # initialize cursor


    def parse_parameter(self):
        """parses the instruction to determine what is the status of the parameter"""
        self.p3, self.p2, self.p1 = [int(x) for x in self.instr[:3]]


    def op1(self):
        """execute OP1: add values of 1st and 2nd index into 3rd index"""
        self.parse_parameter()

        if self.p1:
            if self.p2:
                self.arr[self.arr[self.c + 3]] = self.arr[self.c + 1] + self.arr[self.c + 2]
            else:
                self.arr[self.arr[self.c + 3]] = self.arr[self.c + 1] + self.arr[self.arr[self.c + 2]]
        else:
            if self.p2:
                self.arr[self.arr[self.c + 3]] = self.arr[self.arr[self.c + 1]] + self.arr[self.c + 2]
            else:
                self.arr[self.arr[self.c + 3]] = self.arr[self.arr[self.c + 1]] + self.arr[self.arr[self.c + 2]]

        self.c += 4


    def op2(self):
        """execute OP2: multiply values of 1st and 2nd index into 3rd index"""
        self.parse_parameter()

        if self.p1:
            if self.p2:
                self.arr[self.arr[self.c + 3]] = self.arr[self.c + 1] * self.arr[self.c + 2]
            else:
                self.arr[self.arr[self.c + 3]] = self.arr[self.c + 1] * self.arr[self.arr[self.c + 2]]
        else:
            if self.p2:
                self.arr[self.arr[self.c + 3]] = self.arr[self.arr[self.c + 1]] * self.arr[self.c + 2]
            else:
                self.arr[self.arr[self.c + 3]] = self.arr[self.arr[self.c + 1]] * self.arr[self.arr[self.c + 2]]

        self.c += 4


    def op3(self):
        """takes one input as parameter (the value after it) and stores it in the corresponding index 'arr[parameter]'"""
        self.parse_parameter()

        if self.p1:
            self.arr[self.c + 1] = self.inpt
        else:
            self.arr[self.arr[self.c + 1]] = self.inpt

        self.c += 2


    def op4(self):
        """outputs the value of it's only parameter"""
        self.parse_parameter()

        if self.p1:
            self.diagnostic_code.append(self.arr[self.c + 1])
        else:
            self.diagnostic_code.append(self.arr[self.arr[self.c + 1]])

        self.c += 2


    def op5(self):
        """jumps if true"""
        self.parse_parameter()

        if self.p1:
            if self.p2:
                if self.arr[self.c + 1] != 0:
                    self.c = self.arr[self.c + 2]
                else:
                    self.c += 3
            else:
                if self.arr[self.c + 1] != 0:
                    self.c = self.arr[self.arr[self.c + 2]]
                else:
                    self.c += 3
        else:
            if self.p2:
                if self.arr[self.arr[self.c +1]] != 0:
                    self.c = self.arr[self.c + 2]
                else:
                    self.c += 3
            else:
                if self.arr[self.arr[self.c +1]] != 0:
                    self.c = self.arr[self.arr[self.c + 2]]
                else:
                    self.c += 3


    def op6(self):
        """jumps if false"""
        self.parse_parameter()

        if self.p1:
            if self.p2:
                if self.arr[self.c + 1] == 0:
                    self.c = self.arr[self.c + 2]
                else:
                    self.c += 3
            else:
                if self.arr[self.c + 1] == 0:
                    self.c = self.arr[self.arr[self.c + 2]]
                else:
                    self.c += 3
        else:
            if self.p2:
                if self.arr[self.arr[self.c +1]] == 0:
                    self.c = self.arr[self.c + 2]
                else:
                    self.c += 3
            else:
                if self.arr[self.arr[self.c +1]] == 0:
                    self.c = self.arr[self.arr[self.c + 2]]
                else:
                    self.c += 3


    def op7(self):
        """less then"""
        self.parse_parameter()

        if self.p1:
            if self.p2:
                if self.arr[self.c + 1] < self.arr[self.c + 2]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0
            else:
                if self.arr[self.c + 1] < self.arr[self.arr[self.c + 2]]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0
        else:
            if self.p2:
                if self.arr[self.arr[self.c + 1]] < self.arr[self.c + 2]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0
            else:
                if self.arr[self.arr[self.c + 1]] < self.arr[self.arr[self.c + 2]]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0

        self.c += 4


    def op8(self):
        """equals"""
        self.parse_parameter()

        if self.p1:
            if self.p2:
                if self.arr[self.c + 1] == self.arr[self.c + 2]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0
            else:
                if self.arr[self.c + 1] == self.arr[self.arr[self.c + 2]]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0
        else:
            if self.p2:
                if self.arr[self.arr[self.c + 1]] == self.arr[self.c + 2]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0
            else:
                if self.arr[self.arr[self.c + 1]] == self.arr[self.arr[self.c + 2]]:
                    self.arr[self.arr[self.c + 3]] = 1
                else:
                    self.arr[self.arr[self.c + 3]] = 0

        self.c += 4


    def op_parser(self, *args):
        """parse the instructions executing commands"""
        self.initialize_instrucitons(*args)

        while self.c <= len(self.arr):  #loop with a while statement
            self.instr = f"{self.arr[self.c]:05d}"
            if self.instr[-2:] == '01':
                self.op1()
            if self.instr[-2:] == '02':
                self.op2()
            if self.instr[-2:] == '03':
                self.op3()
            if self.instr[-2:] == '04':
                self.op4()
            if self.instr[-2:] == '05':
                self.op5()
            if self.instr[-2:] == '06':
                self.op6()
            if self.instr[-2:] == '07':
                self.op7()
            if self.instr[-2:] == '08':
                self.op8()
            if self.instr[-2:] == '99':
                break

        return self.arr[0]


    def find_target(self, target):
        """find the noun and verb that satisfy the conditions"""

        for noun in range(100):  # start nested loop
            for verb in range(100):
                if self.op_parser(noun, verb) == target:

                    return 100 * noun + verb


    def get_diagnostic(self):
        """return the final value for the diagnostic code"""

        return self.diagnostic_code[-1]


    def __repr__(self):
        """Check head of file"""

        return ", ".join([str(x) for x in self.data])
