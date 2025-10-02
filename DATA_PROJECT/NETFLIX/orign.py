import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv(
    r"C:\Users\praja\Downloads\Basicpy\DATA_PROJECT\NETFLIX\NetflixOriginals.csv",
    encoding="latin1"
)
df = pd.DataFrame(df)
# print(df.info())
print(df.columns.tolist())

'''
Release_Date       9827 non-null   object 
 1   Title              9827 non-null   object 
 2   Overview           9827 non-null   object 
 3   Popularity         9827 non-null   float64
 4   Vote_Count         9827 non-null   int64  
 5   Vote_Average       9827 non-null   float64
 6   Original_Language  9827 non-null   object 
 7   Genre              9827 non-null   object 
 8   Poster_Url         9827 non-null   object 
 '''
df['Release_Date'] = pd.to_datetime(df['Release_Date'])
df['Release_Date'] = df['Release_Date'].dt.year
print(df['Release_Date'].dtype)