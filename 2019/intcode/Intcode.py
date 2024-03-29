#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Intcode Main Class - refactored
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


class Intcode:
    def __init__(self, data, inpt=1, once=False):
        self.data = [int(x) for x in data.strip().split(",")]
        self.arr = list(self.data)
        self.halt = False
        self.inpt = inpt
        self.once = once  # just output once and then stop
        self.r = 0
        self.outputs = []
        self.output = 0
        self.extend()  # allocate more memory
        self.parse()

    def extend(self):
        """Allocate more memory"""
        memory = [0] * 500
        self.arr += memory

    def evaluate(self, mode, pos):
        """Determine the mode of the instruction"""
        if mode == 0:
            param = self.arr[self.arr[self.c + pos]]
            idx = self.arr[self.c + pos]
        elif mode == 1:
            param = self.arr[self.c + pos]
            idx = self.c + pos
        elif mode == 2:
            param = self.arr[self.arr[self.c + pos] + self.r]
            idx = self.arr[self.c + pos] + self.r
        return (param, idx)

    def op1(self, mode1, mode2, mode3):
        """Addition"""
        val1, _ = self.evaluate(mode1, 1)
        val2, _ = self.evaluate(mode2, 2)
        _, idx3 = self.evaluate(mode3, 3)
        self.arr[idx3] = val1 + val2
        self.c += 4

    def op2(self, mode1, mode2, mode3):
        """Multiplication"""
        val1, _ = self.evaluate(mode1, 1)
        val2, _ = self.evaluate(mode2, 2)
        _, idx3 = self.evaluate(mode3, 3)
        self.arr[idx3] = val1 * val2
        self.c += 4

    def op3(self, mode1, inpt):
        """Input"""
        _, idx1 = self.evaluate(mode1, 1)
        self.arr[idx1] = inpt
        self.c += 2

    def op4(self, mode1):
        """Output"""
        _, idx1 = self.evaluate(mode1, 1)
        self.output = self.arr[idx1]
        self.outputs.append(self.output)
        self.manipulate()
        self.c += 2

    def op5(self, mode1, mode2):
        """Comparison not equal zero"""
        val1, _ = self.evaluate(mode1, 1)
        val2, _ = self.evaluate(mode2, 2)
        if val1 != 0:
            self.c = val2
        else:
            self.c += 3

    def op6(self, mode1, mode2):
        """Comparison equal zero"""
        val1, _ = self.evaluate(mode1, 1)
        val2, _ = self.evaluate(mode2, 2)
        if val1 == 0:
            self.c = val2
        else:
            self.c += 3

    def op7(self, mode1, mode2, mode3):
        """Comparison between parameters arg1 < arg2"""
        val1, _ = self.evaluate(mode1, 1)
        val2, _ = self.evaluate(mode2, 2)
        _, idx3 = self.evaluate(mode3, 3)
        if val1 < val2:
            self.arr[idx3] = 1
        else:
            self.arr[idx3] = 0
        self.c += 4

    def op8(self, mode1, mode2, mode3):
        """Comparison between parameters arg1 == arg2"""
        val1, _ = self.evaluate(mode1, 1)
        val2, _ = self.evaluate(mode2, 2)
        _, idx3 = self.evaluate(mode3, 3)
        if val1 == val2:
            self.arr[idx3] = 1
        else:
            self.arr[idx3] = 0
        self.c += 4

    def op9(self, mode1):
        """Adjusts relative base"""
        val1, _ = self.evaluate(mode1, 1)
        self.r += val1
        self.c += 2

    def getInput(self):
        """apply rules for input"""
        if type(self.inpt) == int:
            return self.inpt
        else:
            if len(self.inpt) == 1:
                return self.inpt[0]
            else:
                res = self.inpt[0]
                self.inpt.pop(0)
                return res

    def parse(self, reset=True):
        """start the main loop that parses the instructions"""
        if reset:
            self.c = 0

        while True:
            self.instr = f"{self.arr[self.c]:05d}"
            self.p3, self.p2, self.p1 = [int(x) for x in self.instr[:3]]

            op = self.instr[-2:]
            if op == "99":
                self.halt = True
                break
            elif op in ["03", "04", "09"]:
                if op == "03":
                    self.instructions[op](self, self.p1, self.getInput())
                elif op == "04":
                    self.instructions[op](self, self.p1)
                    if self.once:
                        break
                else:
                    self.instructions[op](self, self.p1)
            elif op in ["01", "02", "07", "08"]:
                self.instructions[op](self, self.p1, self.p2, self.p3)
            else:
                self.instructions[op](self, self.p1, self.p2)

    instructions = {
        "01": op1,
        "02": op2,
        "03": op3,
        "04": op4,
        "05": op5,
        "06": op6,
        "07": op7,
        "08": op8,
        "09": op9,
    }

    def findTarget(self, target):
        """find the noun and verb that satisfy the target passed"""
        for noun in range(100):
            for verb in range(100):
                self.arr = list(self.data)
                self.arr[1] = noun
                self.arr[2] = verb
                self.parse()
                if self.arr[0] == target:
                    return 100 * noun + verb

    def feedbackInput(self, inpt):
        self.inpt = inpt
        self.once = True
        self.parse(reset=False)

    def manipulate(self):
        pass

    def __repr__(self):
        return ",".join([str(x) for x in self.arr])
