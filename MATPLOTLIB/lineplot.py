import pandas as pd
import matplotlib.pyplot as plt

data = {
    "NAME":[ "John", "Anna", "Peter", "Linda"],
    "AGE":[28, 24, 35, 32],
    "PROFESSION":[ "Engineer", "Doctor", "Artist", "Scientist"],
    "SALARY":[70000, 80000, 50000, 60000],
    "PERFOMANCE":[ 85, 90, 78, 88],
}
df = pd.DataFrame(data)
sort_age = df.sort_values("AGE")
plt.plot(sort_age['AGE'],df["SALARY"], color = "red", marker = "o", linestyle = "--", linewidth = 2, markersize = 8)
plt.title('Line Plot of Age vs Salary')
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.xlabel('Age')
plt.ylabel('Salary')
plt.show()