#!/bin/bash

echo "Cleaning data and output_data folder."

cd data || exit
./clean.sh

cd ..

cd output_data || exit
./clean.sh

cd ..

source env/bin/activate
python3 main.py
