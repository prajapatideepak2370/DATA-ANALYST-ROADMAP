import numpy as np

arr = np.array([1,2,3,4,np.nan,5,6,7,np.nan, np.nan])
print(np.isnan(arr))
# [False False False False  True False False False  True  True]