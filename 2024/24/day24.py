#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day24 2024
"""

__author__ = "gmnr"
__license__ = "GPL"


import helper.advent as aoc

test = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

init, gates = aoc.read_input(sep="\n\n")
wires = {}

for val in init.splitlines():
    k, v = val.split(": ")
    wires[k] = int(v)

operations = []
for g in gates.splitlines():
    v1, op, v2, _, res = g.split()
    operations.append((v1, v2, op, res))

while operations:

    for i, op in enumerate(operations):
        v1, v2 = op[:2]
        if v1 in wires and v2 in wires:
            break

    op = operations.pop(i)
    v1, v2, op, res = op

    if op == "AND":
        r = wires[v1] & wires[v2]
    elif op == "OR":
        r = wires[v1] | wires[v2]
    else:
        r = wires[v1] ^ wires[v2]

    wires[res] = r

# pt 1
zetas = {k: v for k, v in wires.items() if k.startswith("z")}
zetas_keys = sorted(zetas.keys(), reverse=True)
res = ""
for k in zetas_keys:
    res += str(zetas[k])
print(int(res, 2))
