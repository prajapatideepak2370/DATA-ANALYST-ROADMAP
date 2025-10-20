import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
print(s) 
print(s.index) # Default index means 0,1,2,3,...
index = ["Apple", "Mango", "Banana", "Orange", "Strawberry" ]
s.index = index
print(s)
print(s.dtype)
s.name = "Series NUMBERS"

#indexing --- Slycing 
print(s[0])  # Accessing first element using default index
print(s[2:4])  # Slicing from index 2 to 3

# iloc - position based indexing
print(s.iloc[2])
print(s.iloc[[0,2,3]])