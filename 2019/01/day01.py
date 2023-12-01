#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
solution for the first day of the advent of code
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


# get data
with open("input.txt", "r") as f:
    data = f.read().split("\n")[:-1]  # remove the last item which is an empty string

from math import floor


# Part 1
mass = [int(x) for x in data]
fuel_req = sum([floor(x / 3) - 2 for x in mass])

# same result using map
# fuel_req = sum([*map((lambda x: math.floor(int(x) / 3) - 2), data)])

# print solution
# print(fuel_req)


# Part 2
# define a recursive function
def recursive_fuel(mass):
    """recursively apply the mass calculation until the fuel requirement is 0"""

    if mass <= 0:
        return 0
    else:
        return mass + recursive_fuel(floor(mass / 3) - 2)


# apply the funciton
new_fuel_req = sum([recursive_fuel(x) - x for x in mass])
print(new_fuel_req)
