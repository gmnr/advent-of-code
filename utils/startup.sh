#!/bin/bash

# inizialize date and day
YEAR=$(date +"%Y")
DAY=$(date +"%d")

# set root of project folder
ROOT="${HOME}/Coding/advent-of-code/"
ENV_FLD="adv-env/bin/activate"

# run python eng
source $ROOT$ENV_FLD

# execute script 
cd $ROOT"utils"
python get_input.py

# deactivate environement
deactivate

# move to folder
cd $ROOT$YEAR"/"$DAY
