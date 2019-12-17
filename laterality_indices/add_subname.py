import csv
import sys
import os
import subprocess
import glob
import pandas as pd
from pathlib import Path

os.chdir("/home/will/laterality_indices")
pathlist = Path(os.getcwd()).glob('**/*.csv')
for csv_file in pathlist:
     path_in_str = str(csv_file)
     filename = os.path.basename(path_in_str)
     sub_name = filename.split('_')[0].split('-')[1]

     # return each line of csv file as list of strings
     # concatenate those lists into list
     rows = []
     with open(csv_file, 'rt') as f:
         csv_reader = csv.reader(f)
         for line in csv_reader:
            if 'left %' in line:
                del line[0]
            rows.append(line)

     # now add the subject header to the csv csv_file
     header = [sub_name]
     with open (csv_file, 'wt') as f:
         csv_writer = csv.writer(f)
         csv_writer.writerow(header)
         for row in rows:
             csv_writer.writerow(row)
