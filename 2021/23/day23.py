#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
resution for day23 2021
"""

__author__ = "gmnr"
__license__ = "GPL"


with open("input.txt", "r") as f:
    diagram = f.read()

a, b, c, d = 1, 10, 100, 1000

# pt 1
res1 = a * 21 + b * 9 + c * 12 + d * 9
print(res1)

# pt 2
new_lines = """  #D#C#B#A#
  #D#B#A#C#
"""
new_diagram = ""
for i, line in enumerate(diagram.splitlines()):
    if i == 2:
        new_diagram += line + "\n"
        new_diagram += new_lines
    else:
        new_diagram += line + "\n"

res2 = a * 51 + b * 37 + c * 33 + d * 43
print(res2)
