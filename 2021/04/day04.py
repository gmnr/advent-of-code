#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day04 2021
"""

__author__ = "Guido Minieri"
__license__ = "GPL"


with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

extraction = list(map(int, data[0].split(",")))
data.remove(data[0])


def process_boards(data):
    boards = []
    for board in data:
        rows = board.split("\n")
        b = []
        for r in rows:
            if not r:
                continue
            nums = list(map(int, r.split()))
            b.append(nums)
        boards.append(b)
    return boards


def check_win(board):
    for r in board:
        if r == ["X"] * len(r):
            return True
    rev_board = list(map(list, zip(*board)))
    for r in rev_board:
        if r == ["X"] * len(r):
            return True
    return False


# pt 1
boards = process_boards(data)
for called in extraction:
    for B, b in enumerate(boards):
        for R, r in enumerate(b):
            for I, i in enumerate(r):
                if i == called:
                    boards[B][R][I] = "X"

    if any([check_win(x) for x in boards]):
        winner = [x for x in boards if check_win(x)][0]
        sum_others = 0
        for rows in winner:
            for n in rows:
                if n != "X":
                    sum_others += n
        print(called * sum_others)
        break

# pt 2
new_boards = process_boards(data)
for called in extraction:
    for B, b in enumerate(new_boards):
        for R, r in enumerate(b):
            for I, i in enumerate(r):
                if i == called:
                    new_boards[B][R][I] = "X"

    if len(new_boards) == 1 and check_win(new_boards[0]):
        winner = new_boards[0]
        sum_others = 0
        for rows in winner:
            for n in rows:
                if n != "X":
                    sum_others += n
        print(called * sum_others)
        break

    for b in new_boards:
        if check_win(b):
            new_boards.remove(b)
