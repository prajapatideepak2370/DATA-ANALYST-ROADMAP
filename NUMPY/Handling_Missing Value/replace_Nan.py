import numpy as np

arr = np.array([1,2,3,4,np.nan,5,6,7,np.nan, np.nan])
cleaned_arr = np.nan_to_num(arr, nan=0)
print(cleaned_arr)
print(np.isnan(cleaned_arr))