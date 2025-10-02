import pandas as pd
data = {
    "NAME":[ "John", "Anna", "Peter", "Linda"],
    "AGE":[28, 28, 35, 35],
    "PROFESSION":[ "Engineer", "Doctor", "Artist", "Scientist"],
    "SALARY":[70000, 80000, 50000, 60000],
    "PERFOMANCE":[ 85, 90, 78, 88],
    "CITY":[ "New York", "Paris", "Berlin", "London"]
}
df = pd.DataFrame(data)
group_data = df.groupby("AGE")["SALARY"].sum() #It groups the data by AGE and sums the SALARY for each group
multi_group = df.groupby(["AGE","NAME"])["SALARY"].sum() # It Multiple groups the data by both AGE and NAME and sums the SALARY for each group
print("Grouped data by AGE with sum of SALARY:")
print(group_data)
print("\nMulti-level grouping by NAME and AGE with sum of SALARY:")
print(multi_group)