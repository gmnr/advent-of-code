#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
fetch automatically the puzzle for the aoc challanges
in order to work needs a .cookie file with the session cookie for the advent of code site
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import requests
import os

# get the cookie statement
with open('.cookie', 'r') as f:
    cookie = f.read().strip()

# get user data
year = "2019"   # input('What is the year you want to try')
day = input("What day? (day 01 is 1)\n")

# declare url and cookies
cookies = {'session': cookie}
url = f"https://adventofcode.com/{year}/day/{day}/input"

r = requests.get(url, cookies=cookies)
res = r.text

with open('input.txt', 'w') as f:
    f.write(res)

"""
TODO
> automatically create new folders based on the year/number of the challenge
"""
