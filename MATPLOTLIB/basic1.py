import matplotlib.pyplot as plt 
x = ["Mon","Tue","Wed", "Thu", "Fri"]
y = [10, 7,25,9,5]
plt.plot(x, y, linewidth = 2, linestyle = 'dashed', marker = 'o', color = 'green')

plt.title("Weekly sales data")
plt.xlabel("Days of the week")
plt.ylabel("sales in $")
plt.legend(["Sales data"], loc='upper left')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.ylim(0,30)
plt.show()
plt.close()