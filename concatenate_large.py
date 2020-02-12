import pandas as pd
import numpy as np
import os

datadir = "/home/will/Projects/language_laterality/10/language_csvs"
columns = ["subject","task","whole brain left %","broca's area left %","inferior frontal gyrus left %","middle frontal gyrus left %","superior frontal gyrus left %","frontal lobe left %","inferior temporal gyrus left %","middle temporal gyrus left %","superior temporal gyrus left %","planum temporale left %","angular gyrus left %","whole brain right %","broca's area right %","inferior frontal gyrus right %","middle frontal gyrus right %","superior frontal gyrus right %","frontal lobe right %","inferior temporal gyrus right %","middle temporal gyrus right %","superior temporal gyrus right %","planum temporale right %","angular gyrus right %","whole brain LI","broca's area LI","inferior frontal gyrus LI","middle frontal gyrus LI","superior frontal gyrus LI","frontal lobe LI","inferior temporal gyrus LI","middle temporal gyrus LI","superior temporal gyrus LI","planum temporale LI","angular gyrus LI","whole brain left voxels","broca's area left voxels","inferior frontal gyrus left voxels","middle frontal gyrus left voxels","superior frontal gyrus left voxels","frontal lobe left voxels","inferior temporal gyrus left voxels","middle temporal gyrus left voxels","superior temporal gyrus left voxels","planum temporale left voxels","angular gyrus left voxels","whole brain right voxels","broca's area right voxels","inferior frontal gyrus right voxels","middle frontal gyrus right voxels","superior frontal gyrus right voxels","frontal lobe right voxels","inferior temporal gyrus right voxels","middle temporal gyrus right voxels","superior temporal gyrus right voxels","planum temporale right voxels","angular gyrus right voxels","whole brain sum","broca's area sum","inferior frontal gyrus sum","middle frontal gyrus sum","superior frontal gyrus sum","frontal lobe sum","inferior temporal gyrus sum","middle temporal gyrus sum","superior temporal gyrus sum","planum temporale sum","angular gyrus sum","FramewiseDisplacement","tSNR"]

# Get a list of files in directory
onlycsvs = [f for f in os.listdir(datadir) if f.endswith(".csv")]

df_list = [] # Loop through csvs in directory
for file in os.listdir(datadir):
    filename = os.fsdecode(file)
    if filename.endswith(".py"):
        continue
    elif filename.endswith("data.csv"):
        print(filename)
        df = pd.read_csv(os.path.join(datadir,filename), names=columns)
        df_list.append(df)

master_df = pd.concat(df_list, ignore_index=True)
master_df.set_index('subject', drop=True, inplace=True) # change index to subject IDs
master_df.to_csv(os.path.join(datadir, 'language.csv'))
