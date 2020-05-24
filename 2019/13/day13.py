#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 13 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import sys; sys.path.append('..')
from intcode import Intcode


with open('input.txt', 'r') as f:
    data = f.read()


class Game(Intcode):

    def __init__(self, data):
        self.out = []
        self.score = None
        self.width = 36
        self.height = 20
        super().__init__(data)


    def extend(self):
        memory = [0] * 500
        self.arr += memory
        self.arr[0] = 2


    def manipulate(self):
        if len(self.outputs) % 3 == 0 and self.outputs != []:
            x = self.outputs[-3]
            y = self.outputs[-2]
            tile = self.outputs[-1]
            self.out.append([x, y, tile])

            # if tile == 4:
                # if x > 1:
                    # self.inpt = 1
                # elif x < 1:
                    # self.inpt = -1
                # else:
                    # self.inpt = 0

            # if x == -1 and y == 0:  # capture the score of the game
                # self.score = tile


    # def getScore(self):
        # return self.score


    # def play(self):
        # while True:
            # self.c = 0
            # self.parse()
            # if self.findType(2) == 0:
                # break
            # self.getScore()


    def findType(self, tileId):
        res = [x for x in self.out if x[1] == tileId]
        return len(res)


    conv = {
            0: " ",
            1: "W",
            2: "x",
            3: "=",
            4: "O"
    }


    # def __str__(self):
        # """draws the arcade on the screen"""
        # string = ""
        # for line in self.width:
            # for char in self.:





        # return string


arcade = Game(data)
# print(arcade.findType(2))
print(arcade.out)

