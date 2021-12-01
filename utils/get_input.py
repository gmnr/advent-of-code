#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Use this script to download the advent-of-code input file automatically
It requires an hidden .cookie file with the cookies for your advent-of-code session
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from datetime import date
import os
import requests
import sys

# get the root directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# fetch today's date and assign year and day
today = date.today()
year = today.year
month = today.month
day = today.day

# exit the program if there are no challenges today
if month != 12 or day > 25:
    print("There are no challanges today!")
    sys.exit()

# go back to advent-of-code repository
os.chdir('./..')

# move into year folder and create it if it's the first year
if os.path.isdir(f'./{year}'):
    os.chdir(f'./{year}')
else:
    os.mkdir(f'./{year}')
    os.chdir(f'./{year}')

# check if folder exist then create it or move into it (zfill for padding in file name)
foldername = str(day).zfill(2)
if os.path.isdir(f'./{foldername}'):
    os.chdir(f'./{foldername}')
else:
    os.mkdir(f'./{foldername}')
    os.chdir(f'./{foldername}')

# if file exists exit
if os.path.exists('./input.txt'):
    print('Input file has already been downloaded')
    print('Happy Coding!')
    sys.exit()

# get cookies
with open('.cookie', 'r') as f:
    cookie = f.read().strip()
cookies = {'session': cookie}

# fetch data
url = f"https://adventofcode.com/{year}/day/{day}/input"
r = requests.get(url, cookies=cookies)
res = r.text

# write the input puzzle in the input file
with open('input.txt', 'w') as f:
    f.write(res)
print(f'Data fetched: input.txt written in {year}/{day}')
