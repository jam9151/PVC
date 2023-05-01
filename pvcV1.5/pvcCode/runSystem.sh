#!/bin/bash
cd /home/jam/pvcV1.5/pvcCode
rm psheet.xlsx 
cd /home/jam/pvcV1.5/pvcCode
wget https://docs.google.com/spreadsheets/d/e/2PACX-1vQkw4QL7sSO02RJQjjllPTaaQ8vvctJdGscou6b6TicSvBqVixVwrsvDWAeDVqfKzwTHJSooLyrVEjS/pub?output=xlsx -O "psheet.xlsx"
cd /home/jam/pvcV1.5/pvcCode
python3 main.py
