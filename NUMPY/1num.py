import numpy as np

temperatures = np.array([34.6, 36.5, 37.2, 35.8, 33.9])
averge= np.mean(temperatures)
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
print(np.vstack((arr_1, arr_2)))
print()
print(np.hstack((arr_1, arr_2)))      