import matplotlib.pyplot as plt

products = ["Product A", "Product B", "Product C", "Product D"]
sales = [150, 200, 130, 350]

plt.bar(products,sales, color = 'blue', width= 0.3, )
plt.title('Sales of Products ')
plt.xlabel("Products of shops")
plt.ylabel("Sales of the week")
plt.legend(["Sales data"], loc='upper left')
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.ylim(0,400)
plt.show()
plt.close()