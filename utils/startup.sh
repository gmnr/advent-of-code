#!/bin/bash

# inizialize date and day
YEAR=$(date +"%Y")
DAY=$(date +"%d")

# set root of project folder
ROOT="${HOME}/Coding/advent-of-code/"

# execute script 
cd $ROOT"utils"
python3 get_input.py

# move to folder
cd $ROOT$YEAR"/"$DAY
