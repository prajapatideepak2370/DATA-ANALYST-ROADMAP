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
print(df)
# sentax for updating data in the dataframe --- df.loc[row_index, "column_name"] = new_value

df.loc[4, "AGE"] = 20   #---updating only single value in a column
df['SALARY'] = df['SALARY'] * 1.05  # Increasing salary by 5% ---- updating multiple values in a column
print("\nUpdated DataFrame after changing age of Deepak to 20:")
print(df)