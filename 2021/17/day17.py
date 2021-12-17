#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day17 2021
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().strip()

_, ranges = data.split(': ')
x_area, y_area = ranges.split(', ')
x1, x2 = map(int, x_area[2:].split('..'))
y1, y2 = map(int, y_area[2:].split('..'))

target = []
for y in range(y1, y2+1):
    for x in range(x1, x2+1):
        target.append((x, y))

def launch(vel, target):
    v_x, v_y = vel
    x, y = v_x, v_y
    wip = [(x, y)]
    sol = False

    t_max_x = max(c[0] for c in target)
    t_min_x = min(c[0] for c in target)
    t_min_y = min(c[1] for c in target)
    t_max_y = max(c[1] for c in target)

    while (x < t_max_x and y > t_min_y) or (x > t_min_x and y < t_max_y):
        if (x, y) in target:
            sol = True
            break
        elif y < t_min_y:
            break

        if v_x > 0:
            v_x -= 1
        elif v_x < 0:
            v_x += 1
        v_y -= 1

        x += v_x
        y += v_y
        wip.append((x, y))


    if (x, y) in target:
        sol = True
    if (x, y) in target:
        sol = True

    if sol:
        return wip, max(x[1] for x in wip) 
    return sol

# pt 1
res = []
found = set()
for y in range(-300, 300):
    for x in range(300):
        r = launch((x, y), target)
        if r != False:
            print((x, y))
            res.append(r)
            found.add((x, y))
print(max(x[1] for x in res))

# pt 2
print(len(found))
