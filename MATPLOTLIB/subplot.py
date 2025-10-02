import matplotlib.pyplot as plt
x = [1,2,3,4]
y = [10,20,15,35]

fig, ax = plt.subplots(1,2 ,figsize = (10,5))

ax[0].plot(x,y)
ax[0].set_title('LINE CHART')

ax[1].bar(x,y)
ax[1].set_title('BAR CHART')
fig.suptitle("Comparison of Line Chart and Bar chart")
plt.tight_layout()
plt.savefig('comparison.png', dpi = 300, bbox_inches = 'tight')
plt.show()
plt.close()

#now we have to save the chart as a file 
#sentax ---- savefig(filename.Extension , dpi(Dot per inches) = 'value', bbox_inches = 'tight') ------ dpi means image resolution 