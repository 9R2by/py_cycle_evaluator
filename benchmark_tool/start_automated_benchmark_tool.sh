#!/bin/bash

#echo "Cleaning data and output_data folder."
echo "Cleaning data folder"

cd data || exit
./clean.sh

cd ..

cd output_data || exit
./clean.sh

cd ..


source env/bin/activate
# automated/manual 1/0 | pow(2, your value) = n | so/mo
python3 main.py 1 3 so
#python3 main.py 1 3 so
#python3 main.py 1 20 so
#python3 main.py 1 18 so
#python3 main.py 1 10 so
#python3 main.py 1 6 mo
#python3 main.py 1 18 mo
