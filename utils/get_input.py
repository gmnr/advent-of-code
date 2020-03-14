#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Utility scritp that works with crontab to fetch the input puzzle for the current year

Crontab config:
$  crontab -e
$  15 10 1-25 12 * python3 $PATH/advent-of-code/utils/get_input.py > /dev/null 2>&1

## UPDATE: cronjob deprecated...##
"""

__author__ = 'Guido Minieri'
__license__ = 'GPL'


from datetime import date
from time import sleep
import os
import requests


# wait for internet connection to be restored
sleep(12)

# get the directory of the file
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


today = date.today()

year = today.year
day = today.day

with open('.cookie', 'r') as f:
    cookie = f.read().strip()

cookies = {'session': cookie}  # define cookie for the session
url = f"https://adventofcode.com/{year}/day/{day}/input"

# fetch data
r = requests.get(url, cookies=cookies)
res = r.text

os.chdir('./..')  # go back to root dir

# handle year
if not os.path.isdir(f'./{year}'):  # if first day of december
    os.mkdir(f'./{year}')
    os.chdir(f'./{year}')
else:
    os.chdir(f'./{year}')


# zfill for padding
os.mkdir(f'./{str(day).zfill(2)}')
os.chdir(f'./{str(day).zfill(2)}')

with open('input.txt', 'w') as f:
    f.write(res)
