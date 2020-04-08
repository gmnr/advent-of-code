#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 8
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().strip()


class Layer:

    def __init__(self, arr):
        self.arr = arr


    def count(self, val):
        """Return the amount of values in a frame"""

        return len([x for x in self.source if x in val])




class Picture:

    def __init__(self, source, width=25, height=6):
        self.source = list(source)
        self.layers = []
        self.width = width
        self.height = height
        self.compose()


    def compose(self):
        acc = []
        for i in range(len(self.source)):
            acc.append(self.source[i])
            if i % (self.width * self.height) == 0:
                self.layers.append(Layer(acc))
                acc = []

    def check_layers(self, fun, *args):

        res = map(fun(*args), self.layers)
        return list(res)




x = Picture(data)
print(len(x.layers))
