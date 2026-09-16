#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day02 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


from intcode import Intcode

with open("input.txt", "r") as f:
    data = f.read()


def run_intcode(vm):
    process = vm.run()

    try:
        _ = next(process)
    except StopIteration:
        pass
    return vm


new_data = list(data)
new_data[2] = "12"
new_data[4] = "2"
new_data = "".join(new_data)

intcode = Intcode(new_data)
print(run_intcode(intcode).mem[0])


target = 19690720
for noun in range(100):
    for verb in range(100):
        try_data = data.split(",")
        try_data[1] = str(noun)
        try_data[2] = str(verb)
        mem = run_intcode(Intcode(",".join(try_data))).mem[0]
        if mem == target:
            print(100 * noun + verb)
