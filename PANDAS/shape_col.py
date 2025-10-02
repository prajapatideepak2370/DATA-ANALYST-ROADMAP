import pandas as pd
data = {
    "NAME":[ "John", "Anna", "Peter", "Linda"],
    "AGE":[28, 24, 35, 32],
    "PROFESSION":[ "Engineer", "Doctor", "Artist", "Scientist"],
    "SALARY":[70000, 80000, 50000, 60000],
    "PERFOMANCE":[ 85, 90, 78, 88],
    "CITY":[ "New York", "Paris", "Berlin", "London"]

}
df = pd.DataFrame(data)
print (df)
print(f'shape: {df.shape}')
print(f'columns: {df.columns}')