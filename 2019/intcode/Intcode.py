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
        self.halt = False
        self.arr = list(self.data)
        self.inpt = inpt  # defaults to 1
        self.diagnostic_code = []
        self.op_parser()

    def initialize_instrucitons(self, noun=None, verb=None, reset=True):
        """Create a copy of the data, initialize noun/verb and c"""

        if noun != None and verb != None:
            self.arr[1] = noun
            self.arr[2] = verb
        if reset:
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


    def op3(self, inp):
        """takes one input as parameter (the value after it) and stores it in the corresponding index 'arr[parameter]'"""
        self.parse_parameter()

        if self.p1:
            self.arr[self.c + 1] = inp
        else:
            self.arr[self.arr[self.c + 1]] = inp

        self.c += 2


    def op4(self):
        """outputs the value of its only parameter"""
        self.parse_parameter()

        if self.p1:
            self.diagnostic_code.append(self.arr[self.c + 1])
        else:
            self.diagnostic_code.append(self.arr[self.arr[self.c + 1]])

        self.c += 2


    def op5(self):
        """if the first parameter is different than 0 make the cursor equal to the second parameter (or the second parameter value at location)"""
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
        """if the first parameter is equat to 0 make the cursor equal to the second parameter (or the second parameter value at location)"""
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
        """if the first parameter is less than the second parameter change the value of the thrid parameter to 1 else to 0"""
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
        """if the first parameter equal to the second parameter change the value of the thrid parameter to 1 else to 0"""
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


    def op_parser(self, *args, **kwargs):
        """parse the instructions and execute commands"""
        self.initialize_instrucitons(*args, **kwargs)

        while True:
            self.instr = f"{self.arr[self.c]:05d}"
            if self.instr[-2:] == '01':
                self.op1()
            if self.instr[-2:] == '02':
                self.op2()
            if self.instr[-2:] == '03':
                if type(self.inpt) == int:
                    self.op3(self.inpt)
                else:
                    if len(self.inpt) == 1:
                        self.op3(self.inpt[0])
                    else:
                        self.op3(self.inpt[0])
                        self.inpt.pop(0)
            if self.instr[-2:] == '04':
                self.op4()
                break
            if self.instr[-2:] == '05':
                self.op5()
            if self.instr[-2:] == '06':
                self.op6()
            if self.instr[-2:] == '07':
                self.op7()
            if self.instr[-2:] == '08':
                self.op8()
            if self.instr[-2:] == '99':
                self.halt = True
                break
        else:
            print('Compute')

        return None

    def feedback_input(self, inpt):
        self.inpt = inpt
        self.op_parser(reset=False)
        return None


    def find_target(self, target):
        """find the noun and verb that satisfy the target passed"""

        for noun in range(100):  # start nested loop
            for verb in range(100):
                if self.op_parser(noun, verb) == target:

                    return 100 * noun + verb


    def get_diagnostic(self):
        """return the final value for the diagnostic code"""

        return self.diagnostic_code[-1]


    def __repr__(self):
        """print the input file as a string separated by commas"""

        return ", ".join([str(x) for x in self.data])
