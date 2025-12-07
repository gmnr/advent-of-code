#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Docstring
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().strip().split("\n")


class Orbit:
    def __init__(self, center, orbit):
        self.center = center
        self.orbit = orbit
        self.direct = 1
        self.indirect = 0

    @property
    def total(self):
        return self.direct + self.indirect

    def __str__(self):
        return f"{self.center} -> {self.orbit}"

    @classmethod
    def from_string(cls, string):
        center, orbit = string.split(")")
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

    def show(self):
        for orbit in self.coord:
            print(orbit)

    def checksum(self):
        return sum([elem.direct + elem.indirect for elem in self.coord])

    def cleanLine(self, obj):
        arr = []
        while obj.prev != None:
            arr.append(obj)
            obj = obj.prev
        arr.append(obj)  # add last one
        return arr[::-1]

    def findCommonAncestor(self, obj1, obj2):
        arr1 = self.cleanLine(obj1)
        arr2 = self.cleanLine(obj2)

        return [el for el in arr1 if el in arr2][-1]

    def findDistance(self, obj1, obj2):
        return obj1.total - obj2.total


main = Coordinates(data)


# part 1
# print(main.checksum())

# part 2
me = main.findOrbit("YOU")
santa = main.findOrbit("SAN")
common = main.findCommonAncestor(me, santa)

total = (
    main.findDistance(me, common) + main.findDistance(santa, common) - 2
)  # 2 if to account for the fact that you need to reach the center (and not the orbit)
print(total)
