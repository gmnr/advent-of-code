#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day05 2019
"""

__author__ = "gmnr"
__license__ = "GPL"


from intcode import Intcode

with open("input.txt", "r") as f:
    data = f.read()


def run_vm(input):
    vm = Intcode(data)
    process = vm.run(input)
    output = []
    for val in process:

        if val == Intcode.WAITING:
            process.send(input)
        output.append(val)
    return output[-1]


# pt 1
print(run_vm(1))

# pt 2
print(run_vm(5))
