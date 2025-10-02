import numpy as np
arr = np.array([1,2,3,4,np.inf,5,6,7,-np.inf, np.inf])
print(np.isinf(arr))

cleaned_arr = np.nan_to_num(arr, posinf= 50 , neginf= -40)
print(cleaned_arr)
print(np.isinf(cleaned_arr))