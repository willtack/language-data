import csv
import sys
import os
import subprocess
import glob
import pandas as pd
from pathlib import Path

os.chdir("/home/will/laterality_indices")
pathlist = Path(os.getcwd()).glob('**/*.csv')
 # return each line of csv file as list of strings
 # concatenate those lists into list

csv_file='laterality_indices.csv'
rows = []
with open(csv_file, 'rt') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        if 'left %' in line:
            line.insert(0,'') # ADD space in first position
        rows.append(line)

# now add the subject header to the csv csv_file
with open (csv_file, 'wt') as f:
    csv_writer = csv.writer(f)
    for row in rows:
        csv_writer.writerow(row)
