#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Docstring
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


example = "COM)B B)C C)D D)E E)F B)G G)H D)I E)J J)K K)L".split(' ')


with open('input.txt', 'r') as f:
    data = f.read().strip().split('\n')


class Orbit:

    def __init__(self, center, orbit):
        self.center = center
        self.orbit = orbit
        self.direct = 1
        self.indirect = 0


    def __str__(self):
        return f"{self.center} -> {self.orbit}"


    @classmethod
    def from_string(cls, string):
        center, orbit = string.split(')')
        return cls(center, orbit)


    def setPrev(self, prev):
        self.prev = prev
        return self.prev


    def getIndirect(self):
        if self.prev == None:
            return self.indirect
        else:
            return self.prev.getIndirect() + 1


class Coordinates:

    def __init__(self, lst):
        self.data = lst
        self.build()
        self.link()
        self.apply()


    def build(self):
        self.coord = [Orbit.from_string(elem) for elem in self.data]
        return self.coord


    def link(self):
        for elem in self.coord:
            for orb in self.coord:
                if elem.center == orb.orbit:
                    elem.setPrev(orb)
                    break
                elem.setPrev(None)


    def findOrbit(self, string):
        try:
            return [elem for elem in self.coord if string in elem.orbit][0]
        except:
            return None


    def apply(self):
        for elem in self.coord:
            elem.indirect = elem.getIndirect()


    @property
    def show(self):
        for orbit in self.coord:
            print(orbit)

    def checksum(self):
        return sum([elem.direct + elem.indirect for elem in self.coord])


    def leastCommonOrbit(self, obj1, obj2):
        pass


main = Coordinates(data)

# part 1
# print(main.checksum())


# part 2
me = main.findOrbit('YOU')
santa = main.findOrbit('SAN')

print(santa.indirect)
print(me.indirect)
