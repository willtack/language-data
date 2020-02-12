import pandas as pd
import numpy as np
import os

currdir = os.getcwd()

# Get a list of files in directory
onlycsvs = [f for f in os.listdir(currdir) if f.endswith(".csv")]

# Specify column labels

# object
object_cols = ["object","whole brain left %","broca's area left %","inf. frontal left %","mid. frontal left %","planum temporale left %","angular gyrus left %","whole brain right %","broca's area right %","inf. frontal right %","mid. frontal right %","planum temporale right %","angular gyrus right %","whole brain LI","broca's area LI","inf. frontal LI","mid. frontal LI","planum temporale LI","angular gyrus LI","whole brain left voxels","broca's area left voxels","inf. frontal left voxels","mid. frontal left voxels","planum temporale left voxels","angular gyrus left voxels","whole brain right voxels","broca's area right voxels","inf. frontal right voxels","mid. frontal right voxels","planum temporale right voxels","angular gyrus right voxels","FramewiseDisplacement","tSNR"]

# rhyme
rhyme_cols = ["rhyme","whole brain left %","broca's area left %","frontal lobe left %","planum temporale left %","angular gyrus left %","whole brain right %","broca's area right %","frontal lobe right %","planum temporale right %","angular gyrus right %","whole brain LI","broca's area LI","frontal lobe LI","planum temporale LI","angular gyrus LI","whole brain left voxels","broca's area left voxels","frontal lobe left voxels","planum temporale left voxels","angular gyrus left voxels","whole brain right voxels","broca's area right voxels","frontal lobe right voxels","planum temporale right voxels","angular gyrus right voxels","FramewiseDisplacement","tSNR"]

# sentence
sentence_cols = ["sentence","wb left %","ba left %","sup. TG left %","mid. TG left %","inf. TG left %","pt left %","ag left %","wb right %","ba right %","sup. TG right %","mid. TG right %","inf. TG right %","pt right %","ag right %","wb LI","ba LI","sup. TG LI","mid. TG LI","inf. TG LI","pt LI","ag LI","wb left voxels","ba left voxels","sup. TG left voxels","mid. TG left voxels","inf. TG left voxels","pt left voxels","ag left voxels","wb right voxels","ba right voxels","sup. TG right voxels","mid. TG right voxels","inf. TG right voxels","pt right voxels","ag right voxels","FramewiseDisplacement","tSNR"]

# wordgen
wordgen_cols = ["wordgen","whole brain left %","broca's area left %","sfg left %","ifg left %","front left %","pt left %","ag left %","whole brain right %","broca's area right %","sfg right %","ifg right %","front right %","pt right %","ag right %","whole brain LI","broca's area LI","sfg LI","ifg LI","front LI","pt LI","ag LI","whole brain left voxels","broca's area left voxels","sfg left voxels","ifg left voxels","front left voxels","pt left voxels","ag left voxels","whole brain right voxels","broca's area right voxels","sfg right voxels","ifg right voxels","front right voxels","pt right voxels","ag right voxels","FramewiseDisplacement","tSNR"]

# scenemem
scenemem_cols = ["scenemem","mTL left %","hippocampus left %","amygdala left %","phg left %","entorhinal left %","mTL right %","hippocampus right %","amygdala right %","phg right %","entorhinal right %","mTL LI","hippocampus LI","amygdala LI","phg LI","entorhinal LI","mTL left voxels","hippocampus left voxels","amygdala left voxels","phg left voxels","entorhinal left voxels","mTL right voxels","hippocampus right voxels","amygdala right voxels","phg right voxels","entorhinal right voxels","FramewiseDisplacement","tSNR"]


list_of_sentence_dataframes = []
list_of_object_dataframes = []
list_of_rhyme_dataframes = []
list_of_wordgen_dataframes = []
list_of_scenemem_dataframes = []

# Loop through csvs in directory
for file in os.listdir(currdir):
    filename = os.fsdecode(file)
    if filename.endswith(".py"):
        continue
    elif filename.endswith("data.csv"):
        print(filename)
        columns = list(range(39))
        df = pd.read_csv(filename, names=columns)
        #df.fillna("none", inplace=True)
        list_of_sentence_dataframes.append(df.iloc[[0]])
        list_of_object_dataframes.append(df.iloc[[1]])
        list_of_rhyme_dataframes.append(df.iloc[[2]])
        list_of_wordgen_dataframes.append(df.iloc[[3]])
        if len(df.index) > 4:
            list_of_scenemem_dataframes.append(df.iloc[[4]])

# turn the list of DataFrame into one concatenated DataFrame
sentence_df = pd.concat(list_of_sentence_dataframes, ignore_index=True)
object_df = pd.concat(list_of_object_dataframes, ignore_index=True)
rhyme_df = pd.concat(list_of_rhyme_dataframes, ignore_index=True)
wordgen_df = pd.concat(list_of_wordgen_dataframes, ignore_index=True)
scenemem_df = pd.concat(list_of_scenemem_dataframes, ignore_index=True)

# create a list of DataFrames and a list of lists of column names
dfs = [sentence_df, object_df, rhyme_df, wordgen_df, scenemem_df]
col_list = [sentence_cols, object_cols, rhyme_cols, wordgen_cols, scenemem_cols]

# Loop through the lists to do some modifications to axis labels and save to csv
for i in range(0,len(dfs)):
    df = dfs[i]
    for j in range(0,len(col_list)):
        if i==j:
            taskname=col_list[j][0]
            df.dropna(axis=1,how='all',inplace=True) # trim the NaNs at end of shorter DFs
            df.columns = ['subject'] + col_list[j] # get the value (the header list)
            df.rename(columns={taskname:'Task'}, inplace=True) #
            df.set_index('subject', drop=True, inplace=True) # change index to subject IDs
            df.to_csv(os.path.join(currdir, taskname + '.csv'))
