#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solutions for day08 2019
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from matplotlib import pyplot as plt

with open('input.txt', 'r') as f:
    data = f.read().strip()


class Layer:

    def __init__(self, source, width=25, height=6):
        self.source = source
        self.width = width
        self.height = height
        self.out = self.__repr__()

    def findValue(self, value):
        return len([x for x in self.source if x == value])

    def productValues(self, x, y):
        amount1 = self.findValue(x)
        amount2 = self.findValue(y)
        return amount1 * amount2

    def decompose(self):

        res = self.out.split('\n')

        res = [[int(y) for y in x] for x in res]
        return res



    def __repr__(self):
        final = ""

        for i in range(len(self.source)):
            if i == 0:
                final += str(self.source[i])
                continue
            elif i % (self.width) == 0:
                final += '\n'
            final += str(self.source[i])

        return final



class Picture(Layer):

    def __init__(self, source, *args, **kwargs):
        self.source = source

        super().__init__(source, *args, **kwargs)
        self.layers = []
        self.parse_layers()


    def parse_layers(self):

        arr = []

        for i in range(len(self.source)):
            if i == 0:
                arr.append(int(self.source[i]))
                continue
            elif i % (self.width * self.height) == 0:
                self.layers.append(Layer(arr, self.width, self.height))
                arr = []
            arr.append(int(self.source[i]))
        self.layers.append(Layer(arr, self.width, self.height))


    def compose(self):

        image = [None] * self.width * self.height

        for i in range(len(image)):

            for layer in self.layers:
                for j in range(i, len(layer.source)):
                    if j < i:
                        continue
                    else:
                        if layer.source[j] == 2:
                            break
                        else:
                            if image[i] != None:
                                break
                            else:
                                image[i] = layer.source[j]
                                break

            

        return Layer(image, self.width, self.height)


pic = Picture(data)
min_pic = pic.layers[min([(i, x.findValue(0)) for i, x in enumerate(pic.layers)], key = lambda t: t[1])[0]]
# print(min_pic.productValues(1,2))

complete_pic = pic.compose()
print(complete_pic)

message = complete_pic.decompose()
plt.imshow(message)
plt.show()
