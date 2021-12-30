import pandas as pd
from functions import folders
import os

def start_createPool():
    for folder in folders:
        pth = 'texts/'+folder+'/'+'qa/'
        csvs = os.listdir(path = pth)

        csvlist = []
        for csvfile in csvs:
            csvlist.append(pd.read_csv(pth+csvfile))
        pool = pd.concat([csvlist[i] for i in range(len(csvlist))], ignore_index=True)
        pool = pool.drop_duplicates(ignore_index=True)

        pool.to_csv(pth+'pool.csv', index=False)
