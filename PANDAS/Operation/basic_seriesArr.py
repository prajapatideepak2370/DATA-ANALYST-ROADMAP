import pandas as pd

s = pd.Series([10, 20, 30, 40, 50])
print(s) 
print(s.index) # Default index means 0,1,2,3,...
#--------------------------------------------------------------------------------------------
index = ["Apple", "Mango", "Banana", "Orange", "Strawberry" ]
s.index = index
print(s)
print(s.dtype)
s.name = "Series NUMBERS"
#--------------------------------------------------------------------------------------------
# #indexing --- Slycing 
print(s[0])  # Accessing first element using default index
print(s[2:4])  # Slicing from index 2 to 3
#--------------------------------------------------------------------------------------------
# iloc - position based indexing
print(s.iloc[2]) # Single iloc indexing 
print(s.iloc[[0,2,3]]) # Multiple iloc indexing

# loc - Label based indexing 
print(s.loc[['Apple', 'Strawberry']]) # Multiple loc indexing
#--------------------------------------------------------------------------------------------
# In label based indexing your start as well as stop both are included in the output.
print(s["Apple" : "Banana"]) # Slicing from 'Apple' to 'Banana'
