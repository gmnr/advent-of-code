#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 11 of 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


import sys

sys.path.append("..")
from intcode import Intcode
from collections import deque
from matplotlib import pyplot as plt


with open("input.txt", "r") as f:
    data = f.read()


class Robot(Intcode):
    def __init__(self, data, once=False, emerg_hull=False):
        self.coord = [[[0, 0], 0]]
        self.directions = deque(["up", "right", "down", "left"])
        self.direction = None
        self.color = None
        self.painted = 1
        self.emerg_hull = emerg_hull
        self.inpt = None
        super().__init__(data, once)

    def getInput(self):
        """returns the value that goes in input to op3"""
        if self.emerg_hull:
            self.emerg_hull = False
            return 1
        value = self.getCurrentColor()
        return value

    def getCurrentColor(self):
        """returns the color of the tile the robot is standing on"""
        current = self.coord[-1]
        self.sensor_color = current[1]
        return self.sensor_color

    def manipulate(self):
        """allows for the parsing of the 2 intcode outputs: color and rotation"""
        if len(self.outputs) % 2 == 0 and self.outputs != []:
            self.color = self.outputs[-2]
            if self.outputs[-1]:
                self.directions.rotate(-1)
                self.direction = self.directions[0]
            else:
                self.directions.rotate(1)
                self.direction = self.directions[0]
            self.move()

    def findTile(self, x, y):
        """returns the tile if it's tracked, else None"""
        target = [x, y]
        for elem in self.coord[::-1]:
            if elem[0] == target:
                return elem

    def move(self):
        current = self.coord[-1]
        current[1] = self.color

        x, y = current[0]  # get current coordinates

        if self.direction == "up":
            y += 1
        elif self.direction == "right":
            x += 1
        elif self.direction == "down":
            y -= 1
        else:
            x -= 1

        target_tile = self.findTile(x, y)
        if target_tile:
            color = target_tile[1]
        else:
            color = 0
            self.painted += 1
        self.coord.append([[x, y], color])


robot = Robot(data)
print(robot.painted)


# create a new object for part 2
reg_ident = Robot(data, 1, emerg_hull=True)
code = [x[0] for x in reg_ident.coord if x[1] == 1]

x_em = [x[0] for x in code]
y_em = [y[1] for y in code]

plt.scatter(x_em, y_em)
plt.xlim(-3, 43)
plt.ylim(-20, 20)
plt.show()
