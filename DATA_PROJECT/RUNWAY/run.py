import pandas as pd
import numpy as np

df = pd.read_csv('RUNWAYS_PROJECT\Runways_View_-1020707797444363648.csv')

# print(df.describe())
# print(df.info())
df.drop_duplicates(inplace=True)
print(df.isnull().sum())

df.fillna(0, inplace=True)
print(df.head())