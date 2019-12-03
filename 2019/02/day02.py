#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Docstring
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


# get data
with open('input.txt', 'r') as f:
    data = f.read().strip().split(',')


# Part 1
source_opcode = [int(x) for x in data]

def opcode_routine(lst, noun, verb):
    """wrap the opcode routine into a function"""

    arr = list(lst)
    arr[1] = noun
    arr[2] = verb

    for j in range(0, len(arr), 4):
        if arr[j] == 1:
            arr[arr[j + 3]] = arr[arr[j + 1]] + arr[arr[j + 2]]
        if arr[j] == 2:
            arr[arr[j + 3]] = arr[arr[j + 1]] * arr[arr[j + 2]]
        if arr[j] == 99:
            break

    return arr[0]

solution1 = opcode_routine(source_opcode, 12, 2)


# Part 2
expected_result = 19690720

# Loop for all permutations of 2 digits between 0-99
for noun in range(100):
    for verb in range(100):
        if opcode_routine(source_opcode, noun, verb) == expected_result:
            solution2 = 100 * noun + verb
            break
    else:
        continue
    break

# Print the solutions
print(f"The solution for Part 1 is {solution1}")
print(f"The solution for Part 2 is {solution2}")

