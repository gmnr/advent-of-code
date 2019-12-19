#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
fetch automatically the puzzle for the aoc challanges
in order to work needs a .cookie file with the session cookie for the advent of code site
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


import requests
from time import sleep
import os

# get the cookie statement
with open('.cookie', 'r') as f:
    cookie = f.read().strip()
cookies = {'session': cookie}  # declare url and cookies

# years that the aoc has been active
for year in range(2015, 2020):

    # check if the year directory exists
    os.mkdir(f'./{year}')
    os.chdir(f'./{year}')

    # start advent days loop
    for day in range(1, 26):

        os.mkdir(f'./{str(day).zfill(2)}')
        os.chdir(f'./{str(day).zfill(2)}')

        url = f'https://adventofcode.com/{year}/day/{day}/input'
        r = requests.get(url, cookies=cookies)
        res = r.text

        with open('input.txt', 'w') as f:
            f.write(res)

        os.chdir(f'./..')
        print(f"Imported input.txt @ ./{year}/{str(day).zfill(2)}")
        sleep(0.005)



    os.chdir(f'./..')  # go back to root folder



