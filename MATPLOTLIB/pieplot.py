import matplotlib.pyplot as plt

regions = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Oceania']
values = [1638,4584,3453,5324,2332,1234]

plt.pie(values, labels=regions, autopct='%1.1f%%', )
plt.title('Population Distribution by Region')
plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
plt.legend(title='Regions', loc='upper left')
plt.show()
