import pandas as pd
data = {
    "NAME":[ "John", "Anna", "Peter", "Linda", "Deepak", "Sohan", "Manoj" ,"Ashish", "Sumit", "Ravi"],
    "AGE":[28, 24, 35, 32, 29, 30, 31,None, 34, 36],
    "PROFESSION":[ None, "Doctor", "Artist", "Scientist", "Teacher", "Nurse", "Developer", "Designer", "Manager", "Analyst"],
    "SALARY":[70000, 80000, 50000, 60000, 75000, 72000, 68000, 62000, None, 95000],
    "PERFOMANCE":[ 85, 90, 78, 88, None, 87, 80, 91, 95, 89],
    "CITY":[ "New York", None, "Berlin", "London", "Tokyo", "Sydney", "Mumbai", "Dubai", "Toronto", "San Francisco"]
}
df = pd.DataFrame(data)
# now we will handle the missing values using dropna() method 
# dropna() removes rows-column with any missing values 
df.dropna(axis= 0, inplace=True)  #---axis=0 means rows, axis=1 means columns
print(df)

# now we will handle the missing values using fillna() method
# fillna() replaces missing values with a specified value

df.fillna(0, inplace=True)  #--putting 0 in place of missing values (Default value)
df.fillna(value={"PROFESSION": "Unknown", "CITY": "Unknown"}, inplace=True) #--putting custamize value 
df.fillna({'AGE': df['AGE'].mean(),
           'SALARY': df['SALARY'].mean()}, inplace=True)

print("\nDataFrame after filling missing values:")
print(df)

df.to_csv("data_filled.csv", index = False)