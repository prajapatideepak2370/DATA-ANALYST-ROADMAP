import pandas as pd

data = {
    "NAME":[ "John", "Anna", "Peter", "Linda", "Deepak", "Sohan", "Manoj" ,"Ashish", "Sumit", "Ravi"],
    "AGE":[28, 24, 35, 32, 29, 30, 31, 33, 34, 36],
    "PROFESSION":[ "Engineer", "Doctor", "Artist", "Scientist", "Teacher", "Nurse", "Developer", "Designer", "Manager", "Analyst"],
    "SALARY":[70000, 80000, 50000, 60000, 75000, 72000, 68000, 62000, 90000, 95000],
    "PERFOMANCE":[ 85, 90, 78, 88, 82, 87, 80, 91, 95, 89],
    "CITY":[ "New York", "Paris", "Berlin", "London", "Tokyo", "Sydney", "Mumbai", "Dubai", "Toronto", "San Francisco"]
}
df = pd.DataFrame(data)
#print(df)

# INSERTING NEW COLUMN IN THE DATAFRAME 
# SENTAX   df.insert(location,"column name", data)
df.insert(0,"EMPLOYE_ID",[234,534,653,134,245,786,456,223,556,112])
print(df)

# ----------------------------------Removing a column from the dataframe-----------------------------------------
# sentax df.drop(columns =["column_name"], inplace=True )
df.drop(columns =["EMPLOYE_ID"], inplace=True )
print("\nDataFrame after removing the EMPLOYE_ID column:")
print(df)

#-------------------------------------------------------------------------
# iloc and loc to access columns in DataFrame
print(df.iloc[1:3])
print(df.loc[1:3, ['NAME', 'CITY']])

#---Broadcasting a column value to all rows
df["SALARY"] += 1000
print(df.SALARY)
df["SALARY"].unique() # To get unique values in the SALARY column
df["PROFESSION"].value_counts() # To get count of unique values in the PROFESSION column
df["PROMOTED_SALARY"] = df["SALARY"]*10
print(df)