import os, glob
import pandas as pd

path = ".\\Data"

all_files = glob.glob(os.path.join(path, "*.csv"))
df_from_each_file = (pd.read_csv(f, sep=',') for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)

parameter = ['Date', 'HomeTeam', 'AwayTeam', 'FTHG', 'FTAG', 'FTR']
for label in df_merged.columns:
    if (label in parameter):
        continue
    else:
        # https://www.geeksforgeeks.org/delete-a-csv-column-in-python/
        df_merged.pop(label)

df_merged.to_csv(".\\Data\\merged.csv")
