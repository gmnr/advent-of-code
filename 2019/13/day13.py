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

            if tile == 4:
                
                try:
                    px, py, ptile = self.findType(3)[0]
                except:
                    px, py, ptile = [0, 0, 0]

                if x > px:
                    self.inpt = 1
                elif x < px:
                    self.inpt = -1
                else:
                    self.inpt = 0

            if x == -1 and y == 0:  # capture the score of the game
                self.score = tile


    def findType(self, tileId):
        res = [x for x in self.out[::-1] if x[2] == tileId]
        return res

    
    def numBlocks(self):
        listBlocks = self.findType(2)
        return len(listBlocks)


    conv = {0: " ", 1: "W", 2: "x", 3: "=", 4: "O"}


arcade = Game(data)
print(arcade.numBlocks())
print(arcade.score)

