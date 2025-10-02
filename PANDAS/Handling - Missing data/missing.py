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
#checking for null values in the dataframe
print(df.isnull())
# Checking how many null values are present in each column
print(df.isnull().sum())  #--it gives no.of missing values
