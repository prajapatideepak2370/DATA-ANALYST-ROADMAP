import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

arr= np.linspace(1,10,20).reshape(4,5)


# sns.heatmap(arr, annot=True, cmap='coolwarm')
# plt.show()

df = pd.read_csv(r"SEABORN\anagrams.csv")

'''
Data columns (total 5 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   subidr - - int64
 1   attnr  - - object
 2   num1   - - int64
 3   num2   - - float64
 4   num3   - - int64
'''
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.drop(columns=['attnr'], inplace=True)
df.head(10)

sns.heatmap(df, cmap='PuOr',
            annot=True,linewidths=4)
plt.show()