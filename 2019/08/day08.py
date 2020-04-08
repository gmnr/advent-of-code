#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solutions for day08 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().strip()


class Layer:

    def __init__(self, source, width=25, height=6):
        self.source = source
        self.width = width
        self.height = height

    def findValue(self, value):
        return len([x for x in self.source if x == value])

    def productValues(self, x, y):
        amount1 = self.findValue(x)
        amount2 = self.findValue(y)
        return amount1 * amount2


class Picture(Layer):

    def __init__(self, source, *args, **kwargs):
        self.source = source

        super().__init__(source, *args, **kwargs)
        self.layers = []
        self.compose()


    def compose(self):

        arr = []

        for i in range(len(self.source)):
            if i == 0:
                arr.append(int(self.source[i]))
                continue
            elif i % (self.width * self.height) == 0:
                self.layers.append(Layer(arr))
                arr = []
            arr.append(int(self.source[i]))
        self.layers.append(Layer(arr))


pic = Picture(data)
min_pic = pic.layers[min([(i, x.findValue(0)) for i, x in enumerate(pic.layers)], key = lambda t: t[1])[0]]

print(min_pic.productValues(1,2))
