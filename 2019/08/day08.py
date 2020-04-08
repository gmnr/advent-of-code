#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
<<<<<<< Updated upstream
solution for day 8
=======
Solutions for day08 2019
>>>>>>> Stashed changes
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().strip()


class Layer:

<<<<<<< Updated upstream
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
=======
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
>>>>>>> Stashed changes
        self.compose()


    def compose(self):
<<<<<<< Updated upstream
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
=======

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
>>>>>>> Stashed changes
