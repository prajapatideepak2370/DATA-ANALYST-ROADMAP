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

#sorting data
#sentax --- df.sort_values(by = "column_name", ascending = True/False, inplace = True/False)

# df.sort_values(by="NAME", ascending=True, inplace= True )  #Targeting single column only for sorting 

df.sort_values(by = ["AGE", "NAME" , "SALARY"], ascending = [True, True, True], inplace = True)  #Targeting multiple columns for sorting
print('AFTER SORTING --- ')
print(df)