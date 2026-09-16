#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day13 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


from collections import defaultdict
from intcode import Intcode

with open("input.txt", "r") as f:
    data = f.read()

# pt1
game = defaultdict(list)
vm = Intcode(data)
process = vm.run()

try:
    while not vm.halted:
        x = next(process)
        y = next(process)
        id = next(process)

        game[id].append((x, y))

except StopIteration:
    pass

print(len(game[2]))

# pt2
vm = Intcode("2" + data[1:])
process = vm.run()

score = 0
paddle_x = 0
ball_x = 0

try:
    val = next(process)

    while not vm.halted:

        if val == Intcode.WAITING:
            joystick = (ball_x > paddle_x) - (ball_x < paddle_x)
            val = process.send(joystick)
            continue

        x = val
        y = next(process)
        tile = next(process)

        if x == -1 and y == 0:
            score = tile
        elif tile == 3:
            paddle_x = x
        elif tile == 4:
            ball_x = x

        val = next(process)

except StopIteration:
    pass

print(score)
