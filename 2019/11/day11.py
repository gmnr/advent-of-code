#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 11 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import sys; sys.path.append('..')
from intcode import Intcode
from itertools import cycle


with open('input.txt', 'r') as f:
    data = f.read()


class Robot(Intcode):

    def __init__(self, data, inpt=1, once=False):
        super().__init__(data, inpt, once)
        self.coord = [((0, 0), 'up')]
        self.directions = cycle(['right', 'down', 'left', 'up'])
        self.execute()


    def getInput(self):
        """apply rules for input"""
        if len(self.coord) == 1:
            return self.inpt


    def parse(self):
        """Defuse Parent method at launch"""
        pass


    def move(self):
        """calculate the exact coordinates"""
        color, rot = inst
        pcoord, face = coord[-1]
        x, y = pcoord
        if rot:
            ndir = next(direct)
            if ndir == 'up':
                y += 1
            elif ndir == 'right':
                x += 1
            elif ndir == 'down':
                y -= 1
            else:
                x -=1
            coord.append(((x,y), ndir))
        else:
            if face == 'up':
                y += 1
            elif face == 'right':
                x += 1
            elif face == 'down':
                y -= 1
            else:
                x -=1
            coord.append(((x,y), face))



    def execute(self):
        """start the main loop that parses the instructions"""
        self.c = 0
        while True:
            self.instr = f"{self.arr[self.c]:05d}"
            self.p3, self.p2, self.p1 = [int(x) for x in self.instr[:3]]
            op = self.instr[-2:]
            if op == '99':
                self.halt = True
                break
            elif op in ['03', '04', '09']:
                if op == '03':
                    self.instructions[op](self, self.p1, self.getInput())
                elif op == '04':
                    self.instructions[op](self, self.p1)
                    if self.outputs % 2 == 0:
                        try:
                            self.coord.append()
                else:
                    self.instructions[op](self, self.p1)
            elif op in ['01', '02', '07', '08']:
                self.instructions[op](self, self.p1, self.p2, self.p3)
            else:
                self.instructions[op](self, self.p1, self.p2)

    # you need to implement a total new parse module that accounts for the color of the tile the robot is under

    # you can reuse some of the component and instructions below

def mapInputs(arr):
    res = []
    for i in range(len(arr)):
        if i % 2 == 0:
            res.append((arr[i], arr[i+1]))
    return res


robot = Robot(data)
print(robot.coord)

# for inst in instructions:
    # color, rot = inst
    # pcoord, face = coord[-1]
    # x, y = pcoord
    # if rot:
        # ndir = next(direct)
        # if ndir == 'up':
            # y += 1
        # elif ndir == 'right':
            # x += 1
        # elif ndir == 'down':
            # y -= 1
        # else:
            # x -=1
        # coord.append(((x,y), ndir))
    # else:
        # if face == 'up':
            # y += 1
        # elif face == 'right':
            # x += 1
        # elif face == 'down':
            # y -= 1
        # else:
            # x -=1
        # coord.append(((x,y), face))
# print(coord)

# unique_coord = set(list(map(lambda x: x[0], coord[:-1])))
# print(unique_coord)


