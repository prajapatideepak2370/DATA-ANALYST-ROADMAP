import matplotlib.pyplot as plt

score = [56,75,45,76,89,90,67,78,88,95,80,70,60,85,92,73,82,91,68,77,84,66,69,72,81]
plt.hist(score, bins=5, color='blue', edgecolor='black')
plt.xlabel('SCORE RANGE')
plt.ylabel('FREQUENCY')
plt.title('Score Distribution Histogram')
plt.grid(axis='y', alpha=0.75)
plt.legend(['Score Distribution'], loc='upper left')
plt.show()
plt.close()