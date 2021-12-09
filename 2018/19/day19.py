#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day16 2018
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'

with open('input.txt', 'r') as f:
    data = f.read().splitlines()

import re
import collections

def parse(data):
    instructions = []
    for line in data:
        inst, *args = line.split()
        args = list(map(int, args))
        instructions.append((inst, *args))
    return instructions

def addr(a, b, c, reg):
    reg[c] = reg[a] + reg[b]
    return reg

def addi(a, b, c, reg):
    reg[c] = reg[a] + b
    return reg

def mulr(a, b, c, reg):
    reg[c] = reg[a] * reg[b]
    return reg

def muli(a, b, c, reg):
    reg[c] = reg[a] * b
    return reg

def banr(a, b, c, reg):
    reg[c] = reg[a] & reg[b]
    return reg

def bani(a, b, c, reg):
    reg[c] = reg[a] & b
    return reg

def borr(a, b, c, reg):
    reg[c] = reg[a] | reg[b]
    return reg

def bori(a, b, c, reg):
    reg[c] = reg[a] | b
    return reg

def setr(a, b, c, reg):
    reg[c] = reg[a]
    return reg

def seti(a, b, c, reg):
    reg[c] = a
    return reg

def gtir(a, b, c, reg):
    if a > reg[b]: reg[c] = 1
    else: reg[c] = 0
    return reg

def gtri(a, b, c, reg):
    if reg[a] > b: reg[c] = 1
    else: reg[c] = 0
    return reg

def gtrr(a, b, c, reg):
    if reg[a] > reg[b]: reg[c] = 1
    else: reg[c] = 0
    return reg

def eqir(a, b, c, reg):
    if a == reg[b]: reg[c] = 1
    else: reg[c] = 0
    return reg

def eqri(a, b, c, reg):
    if reg[a] == b: reg[c] = 1
    else: reg[c] = 0
    return reg

def eqrr(a, b, c, reg):
    if reg[a] == reg[b]: reg[c] = 1
    else: reg[c] = 0
    return reg

def run(instructions, pointer, reg_zero='0'):
    reg = [int(x) for x in reg_zero + '00000']
    p_reg = pointer[1]


    fn = {
            'addr': addr,
            'addi': addi,
            'mulr': mulr,
            'muli': muli,
            'banr': banr,
            'boni': bani,
            'borr': borr,
            'bori': bori,
            'setr': setr,
            'seti': seti,
            'gtir': gtir,
            'gtri': gtri,
            'gtrr': gtrr,
            'eqir': eqir,
            'eqri': eqri,
            'eqrr': eqrr
    }

    p = 0

    while True:
        try:
            instr = instructions[p]
            f, *vals = instr
        except:
            return reg

        reg[p_reg]  = p
        reg = fn[f](*vals, reg)

        p = reg[p_reg]
        p += 1

# pt 1
pointer, *instr = parse(data)
# res = run(instr, pointer)
# print(res[0])

# pt 2
a,b = map(int, [re.findall('\d+', data[i])[1] for i in [22, 24]])
number_to_factorize = 10551236 + a * 22 + b

factors = collections.defaultdict(lambda: 0)
possible_prime_divisor = 2
while possible_prime_divisor ** 2 <= number_to_factorize:
	while number_to_factorize % possible_prime_divisor == 0:
		number_to_factorize /= possible_prime_divisor
		factors[possible_prime_divisor] += 1 
	possible_prime_divisor += 1

if number_to_factorize > 1:
	factors[number_to_factorize] += 1

sum_of_divisors = 1
for prime_factor in factors:
	sum_of_divisors *= (prime_factor ** (factors[prime_factor] + 1) - 1) / (prime_factor - 1)

print(int(sum_of_divisors))
