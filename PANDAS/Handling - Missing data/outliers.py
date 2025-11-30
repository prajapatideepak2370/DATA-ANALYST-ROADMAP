# OUTLIERS REMOVE BY IQR METHOD 

import pandas as pd

# Example dataset
data = pd.DataFrame({'values': [10, 12, 11, 13, 500, 14, 15]})

Q1 = data['values'].quantile(0.25)
Q3 = data['values'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Remove outliers
clean_data = data[(data['values'] >= lower) & (data['values'] <= upper)]

print("Cleaned Data:")
print(clean_data)
