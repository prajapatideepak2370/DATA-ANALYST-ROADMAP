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

# Interpolating missing values in the DataFrame
# df.interpolate(method='linear', inplace=True)
df['AGE'] = df['AGE'].interpolate(method='polynomial', order=1)
#---There are many methods for interpolation like 'linear', 'time', 'index', 'nearest', 'polynomial', 'spline', 'pchip',etc.
print("DataFrame after interpolating missing values:")
print(df)

df.to_json("data_interpolated.json", orient = "records", lines = True)