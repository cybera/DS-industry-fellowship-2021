#!/bin/bash

TIME1=`date +%Y-%m-%d_%H-%M-%S`

echo "Current working directory: `pwd`"
echo "Starting run at: " ${TIME1}


echo "Running Python script to download data"

python my_first_script.py


echo "End of script"

git add Master5rows.csv
git commit "Don't upload data to GitHub, I am just demoing"
git push origin main