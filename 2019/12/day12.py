#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for day 12 2019
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


from itertools import combinations
import numpy


with open("input.txt", "r") as f:
    data = f.read()[:-1]


class Moon:
    def __init__(self, x, y, z):
        self.pos_x = x
        self.pos_y = y
        self.pos_z = z

        self.vel_x = 0
        self.vel_y = 0
        self.vel_z = 0

    def potential(self):
        return abs(self.pos_x) + abs(self.pos_y) + abs(self.pos_z)

    def kinetic(self):
        return abs(self.vel_x) + abs(self.vel_y) + abs(self.vel_z)

    def total(self):
        return self.potential() * self.kinetic()

    @classmethod
    def fromString(cls, string):
        x, y, z = [x[x.index("=") + 1 : -1] for x in string.split(" ")]
        return cls(int(x), int(y), int(z))


class Cluster:
    def __init__(self, source):
        self.obs = [Moon.fromString(x) for x in source.split("\n")]
        self.axis = ["x", "y", "z"]
        self.ax = None
        self.periods = []

    def applyG(self, pairs, axis):
        moon1, moon2 = pairs

        if axis == "x":
            if moon1.pos_x > moon2.pos_x:
                moon1.vel_x -= 1
                moon2.vel_x += 1
            elif moon1.pos_x < moon2.pos_x:
                moon2.vel_x -= 1
                moon1.vel_x += 1

        elif axis == "y":
            if moon1.pos_y > moon2.pos_y:
                moon1.vel_y -= 1
                moon2.vel_y += 1
            elif moon1.pos_y < moon2.pos_y:
                moon2.vel_y -= 1
                moon1.vel_y += 1

        else:
            if moon1.pos_z > moon2.pos_z:
                moon1.vel_z -= 1
                moon2.vel_z += 1
            elif moon1.pos_z < moon2.pos_z:
                moon2.vel_z -= 1
                moon1.vel_z += 1

    def applyV(self, moon, ax):
        if ax == "x":
            moon.pos_x += moon.vel_x

        elif ax == "y":
            moon.pos_y += moon.vel_y

        else:
            moon.pos_z += moon.vel_z

    def stepTime(self, axis=["x", "y", "z"]):
        for ax in axis:
            for pair in combinations(self.obs, 2):
                self.applyG(pair, ax)

            for moon in self.obs:
                self.applyV(moon, ax)

    def scan(self, n=1000):
        for _ in range(n):
            self.stepTime()

    def totalEnergy(self):
        res = [x.total() for x in self.obs]
        return sum(res)

    def __hash__(self):
        if self.ax == "x":
            val = [(moon.pos_x, moon.vel_x) for moon in self.obs]
        elif self.ax == "y":
            val = [(moon.pos_y, moon.vel_y) for moon in self.obs]
        else:
            val = [(moon.pos_z, moon.vel_z) for moon in self.obs]
        return hash(tuple(val))

    def period(self, axis):
        self.ax = axis
        n = 0
        states = [self.__hash__()]
        while True:
            self.stepTime(axis)
            curr = self.__hash__()
            n += 1
            if curr in states:
                break
            states.append(curr)
        self.periods.append(n)

    def runStates(self):
        for ax in self.axis:
            self.period(ax)

        res = self.findLCM()
        return res

    def findLCM(self):
        return numpy.lcm.reduce(self.periods)


jupiter = Cluster(data)
jupiter.scan()
print(jupiter.totalEnergy())
print(jupiter.runStates())
