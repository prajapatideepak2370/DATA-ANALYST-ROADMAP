import pandas as pd #this lib is use to manipulate data and clean the data 
import numpy as np # thuis lib is use to perform numerical operations and array manipulation
import matplotlib.pyplot as plt # this lib is use to create static, animated, and interactive visualizations in Python
import seaborn as sns # this lib is use to create statistical data visualization

df = pd.read_excel(r"DATA_PROJECT\100_PEOPLE\100 People.xlsx", engine="openpyxl")
df = pd.DataFrame(df)

#print(df.isnull().sum()) # Check for missing values in the DataFrame
df.drop_duplicates(inplace = True) # Remove duplicate rows from the DataFrame
print(df.info()) # Display information about the DataFrame
# print(df)
#--------------------------------------------------------------BAR PLOT--------------------------------------------------------------------
print(df.columns.tolist())
plt.bar(df['Category'], df['Value'], color='red', width=0.4)
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('100 People Data Analysis')
plt.xticks(rotation=35)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend(['Analyis graph 2025'], loc='upper right')
plt.ylim(0, 100)
plt.tight_layout()
# Save the plot as a PNG file
plt.savefig('100_people_data_analysis.png', dpi=300, bbox_inches='tight')
#-------------------------------------------------------------PIE CHART--------------------------------------------------------------------------
plt.figure(figsize=(8, 8))
plt.pie(
    df['Value'], 
    labels=df['Subcategory'], 
    autopct='%1.1f%%', 
    startangle=140
)
plt.tight_layout()
plt.title("Distribution by Subcategory")
sns.lineplot(x='Category', y='Value', data = df, size = 30)
# plt.show()
# plt.close()
print(df)
df.dropna(inplace=True)
print(df.isnull().sum())