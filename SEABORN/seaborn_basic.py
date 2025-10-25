import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
print(os.getcwd())


df = pd.read_csv(r"C:\Users\praja\OneDrive\Codes_Project\DATA ANALYST\DATA-ANALYST-ROADMAP\SEABORN\penguins.csv")
df = pd.DataFrame(df)
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(df.isna().sum())

print(df.head())
'''
 0   species            344 non-null    object 
 1   island             344 non-null    object 
 2   bill_length_mm     342 non-null    float64
 3   bill_depth_mm      342 non-null    float64
 4   flipper_length_mm  342 non-null    float64
 5   body_mass_g        342 non-null    float64
 6   sex                333 non-null    object 
#  '''


#------------------------------------------------------------LINE PLOT SENTAX--------------------------------------------------------------------------
sns.lineplot(x='bill_length_mm', y='bill_depth_mm', data=df, hue='sex', markers=["o",">"], palette='Accent', style='sex')
plt.title("Penguin Bill Length vs Depth")
plt.show()

#--------------------------------------------------------------BAR PLOT SENTAX---------------------------------------------------------------------------
sns.barplot(x='island', y = 'body_mass_g', data = df,hue='sex'
            '''ci=100,n_boot=2''',
            palette='Set2', estimator=np.mean)
plt.title("Penguin Species by Island")
plt.show()

#--------------------------------------------------------------HISTOGRAM SENTAX---------------------------------------------------------------------------
sns.histplot(
    df['flipper_length_mm'],
    bins=[170, 180, 190, 200, 210, 220, 230, 240],
    color='red',           # histogram color
    kde=True, 
    stat='density',
    multiple='stack',
    line_kws={'color': 'green', 'linewidth': 2}  # KDE line styling
)
plt.show()
#--------------------------------------------------------------SCATTER PLOT SENTAX---------------------------------------------------------------------------

sns.scatterplot(
    x='bill_length_mm', y='bill_depth_mm',
    data=df, hue='sex', style='sex', size='sex',
    sizes=(20,40), dodge=True, jitter=True, palette='Set1'
)
  # Jitter adds random noise to the data points to prevent overlap and Dodge separates overlapping points
sns.set_context("notebook")
plt.title("Penguin Bill Length vs Depth")
sns.despine(left =True, bottom=True) # means removing the top and right border
plt.show()
plt.close()
#--------------------------------------------------------------SWARM PLOT SENTAX---------------------------------------------------------------------------
sns.swarmplot(x="species", y="body_mass_g", hue="island", data=df,
              palette="Set2", dodge=True, markersize=6)
plt.show()
plt.close()
#--------------------------------------------------------------COUNTPLOT SENTAX---------------------------------------------------------------------------
# SENTEX --  sns.countplot(x='column_Name ', data=df, hue ="column_Name", )
sns.countplot(x='species', data=df, hue='island', palette='Set3')
plt.show()

#--------------------------------------------------------------REGRESSION PLOT---------------------------------------------------------------------------
sns.regplot(x='body_mass_g', y='flipper_length_mm', data=df,
            scatter_kws={'color':'blue', 's':20},
            line_kws={'color':'red', 'linewidth':2})
plt.show()
plt.close()
#--------------------------------------------------------------JOINT PLOT SENTAX---------------------------------------------------------------------------
sns.jointplot(x='bill_length_mm', y='bill_depth_mm', data=df,
              kind='hex', color='purple', height=8)
plt.show()
plt.close()