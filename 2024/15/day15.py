#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day15 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

test = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

test = """#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
"""

data = aoc.read_input(test, sep="\n\n")


def visual(g, w, c):
    for y in range(7):
        s = ""
        for x in range(13):
            if (x, y) in w:
                s += "#"
            elif (x, y) == c:
                s += "@"
            else:
                s += g[(x, y)]
        print(s)


maze, moves = data
moves = "".join(moves.splitlines())

grid = {}
walls = set()
c = tuple()

for y, line in enumerate(maze.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            walls.add((x, y))
        else:
            if char == "@":
                grid[(x, y)] = "."
                c = (x, y)
                continue
            grid[(x, y)] = char

DIR = {"<": (-1, 0), "^": (0, -1), ">": (1, 0), "v": (0, 1)}


# pt 1
for m in moves:
    new_c = tuple(map(sum, zip(c, DIR[m])))
    if new_c in walls:
        continue
    elif grid[new_c] == "O":
        c_boxes = new_c
        cnt = 0
        to_move = []

        while True:
            c_boxes = tuple(map(sum, zip(c_boxes, DIR[m])))
            cnt += 1
            to_move.append(c_boxes)

            if c_boxes in walls:
                to_move = []
                break

            if grid[c_boxes] == ".":
                break

        if not to_move:
            continue
        else:
            grid[new_c] = "."
            c = new_c
            for i, b in enumerate(to_move):
                grid[b] = "O"

    else:
        c = new_c

coords = [k for k, v in grid.items() if v == "O"]
total = 0
for c in coords:
    x, y = c
    total += y * 100 + x
print(total)

# pt 2
bgrid = {}
bwalls = set()
c = tuple()

new_maze = ""
for line in maze.splitlines():
    for x in line:
        if x == "#":
            new_maze += "##"
        elif x == "O":
            new_maze += "[]"
        elif x == ".":
            new_maze += ".."
        else:
            new_maze += "@."
    new_maze += "\n"
print(new_maze)

for y, line in enumerate(new_maze.splitlines()):
    for x, char in enumerate(line):
        if char == "#":
            bwalls.add((x, y))
        else:
            if char == "@":
                bgrid[(x, y)] = "."
                c = (x, y)
                continue
            bgrid[(x, y)] = char

print(moves)
for m in moves:
    new_c = tuple(map(sum, zip(c, DIR[m])))
    if new_c in bwalls:
        continue
    elif bgrid[new_c] in ("]", "["):
        c_boxes = new_c
        cnt = 0
        to_move = []

        while True:
            c_boxes = tuple(map(sum, zip(c_boxes, DIR[m])))
            cnt += 1
            to_move.append(c_boxes)

            if c_boxes in bwalls:
                to_move = []
                break

            if bgrid[c_boxes] == ".":
                break

        if not to_move:
            continue
        else:
            bgrid[new_c] = "."
            c = new_c
            for i, b in enumerate(to_move):
                bgrid[b] = "X"
    else:
        c = new_c

    print("move", m)
    visual(bgrid, bwalls, c)
    print()
