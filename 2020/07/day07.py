#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Solution for day 7 2020
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


with open('input.txt', 'r') as f:
    data = f.read().split('\n')[:-1]

from collections import defaultdict
import re

TARGET = 'shiny gold'
seen = defaultdict(int)
seen[TARGET] = 1

def list_keys(dct):
    return list(dct.keys())

while True:
    old_len = len(set(seen))
    for rule in data:
        bag, bags = rule.split(' contain ')
        if any([x in bags for x in list_keys(seen)]):
            seen[bag[:-1]] = 1
    if old_len == len(list_keys(seen)):
        break

def parse_bag_rules(rules):
    bag_rules = defaultdict(list)
    for rule in rules:
        bag_name, contents = rule.split(" bags contain ")
        if "no" in contents: continue
        inner_bags = contents.split(", ")
        for bag in inner_bags:
            num, attribute, color, *_ = bag.split(" ")
            bag_rules[bag_name] += [f"{attribute} {color}"] * int(num)
    return bag_rules

def get_bag_count_for(bag_rules, my_bag="shiny gold"):
    bag_count = 0
    for bag in bag_rules[my_bag]:
        bag_count += 1 + get_bag_count_for(bag_rules, bag)
    return bag_count

# pt 1
print(len(set(seen)) - 1)
# pt 2
bag_rules = parse_bag_rules(data)
print(get_bag_count_for(bag_rules))
