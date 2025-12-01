#!/bin/bash

# inizialize date and day
YEAR=$(date +"%Y")
DAY=$(date +"%d")
URL_DAY=$(date +"%-d")

# set root of project folder
ROOT="${HOME}/Documents/advent-of-code/"

# execute script 
cd $ROOT"utils"
python3 get_input.py

# if is the year of the advent open last puzzle, else open nvim in root
cd $ROOT
if cd $YEAR ; then
  cd $DAY
  open "https://adventofcode.com/$YEAR/day/$URL_DAY"
  nvim "day$DAY.py"
else
  nvim
fi
