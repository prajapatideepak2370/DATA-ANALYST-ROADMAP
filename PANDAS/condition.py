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
print('Sample Dataframe:')
#---------------------------------------------- PRINTING COLUMN -----------------------------------------------------------------#
print("NAME (single column return series)") #---     \
name = df['NAME']                           #   ----- > printing the name of single column in the given dataframe using conditon 
#print(name)                                 #---     /          

#selecting multiple columns using condition

subset = df[["NAME","PROFESSION"]]
#print('\nSubset of dataframe')
#print(subset)

#------------------------------------------------- Filtering Rows -----------------------------------------------------------------#

hightest_salary = df[df['SALARY'] > 80000]
#print('\nEmployees with salary greater than 45000:')
#print(hightest_salary)

filter = df[(df['AGE']>30) & (df['SALARY']>60000)]
print('\nEmployees with age greater than 30 and salary greater than 60000:')
print(filter)