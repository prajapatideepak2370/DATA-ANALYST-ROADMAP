import pandas as pd
#pd.concat() is used to concatenate two or more dataframes along a particular axis (rows or columns).
data_1 = pd.DataFrame({
    "Name": ["John", "Anna", "Peter"],
    "Age": [28, 28, 35],
    "City": ["New York", "Paris", "Berlin"]
})

data_2 = pd.DataFrame({
    "Name": ["Linda", "James"],
    "Age": [35, 40],
    "City": ["London", "Madrid"]
})

# Concatenating dataframes along rows (axis=0) vertically
concat_data_rows = pd.concat([data_1,data_2], axis = 0, ignore_index= True)
print(concat_data_rows)
print()
# Concatenating dataframes along columns (axis=1) horizontally
concat_data_columns = pd.concat([data_1,data_2], axis = 1, ignore_index=True)
print(concat_data_columns)