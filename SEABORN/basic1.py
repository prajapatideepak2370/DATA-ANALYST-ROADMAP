import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"SEABORN\penguins.csv")
df = pd.DataFrame(df)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
# print(df.isna().sum())

# print(df.head())
'''
 0   species            344 non-null    object 
 1   island             344 non-null    object 
 2   bill_length_mm     342 non-null    float64
 3   bill_depth_mm      342 non-null    float64
 4   flipper_length_mm  342 non-null    float64
 5   body_mass_g        342 non-null    float64
 6   sex                333 non-null    object 
 '''

#------------------------------------------------------------LINE PLOT SENTAX--------------------------------------------------------------------------
# sns.lineplot(x='bill_length_mm', y='bill_depth_mm', data=df, hue='sex', markers=["o",">"], palette='Accent', style='sex')
# plt.title("Penguin Bill Length vs Depth")
# plt.show()

#--------------------------------------------------------------BAR PLOT SENTAX---------------------------------------------------------------------------
# sns.barplot(x='island', y = 'body_mass_g', data = df,hue='sex'
#             '''ci=100,n_boot=2''',
#             palette='Set2')
# plt.title("Penguin Species by Island")
# plt.show()

#--------------------------------------------------------------HISTOGRAM SENTAX---------------------------------------------------------------------------
# sns.histplot(
#     df['flipper_length_mm'],
#     bins=[170, 180, 190, 200, 210, 220, 230, 240],
#     color='red',           # histogram color
#     kde=True, 
#     stat='density',
#     line_kws={'color': 'green', 'linewidth': 2}  # KDE line styling
# )
# plt.show()
#--------------------------------------------------------------SCATTER PLOT SENTAX---------------------------------------------------------------------------

sns.scatterplot(x='bill_length_mm', y='bill_depth_mm',
                 data=df, hue='sex', 
                style='sex',size='sex',
                sizes=(20,40))

plt.title("Penguin Bill Length vs Depth")
plt.show()
plt.close()
#--------------------------------------------------------------COUNTPLOT SENTAX---------------------------------------------------------------------------

#SENTEX --  sns.countplot(x='column_Name ', data=df, hue ="column_Name", )
