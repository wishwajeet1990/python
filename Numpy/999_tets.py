import numpy as np

arr = np.array([[-1 ,- 7 , 8 , 2 , 3 , 4 , 5],[10 , -70 , 80 , -20 , 30 , -40 , 50],[100 , 700 , -800 , 200 , 300 , -400 , 500]])
print("arr = ",arr)
mask = arr > 3
print("arr > 3 = ",arr[mask])  # Elements greater than 3
print("Shape = ",np.shape(arr))
print("Absolute  = ",np.absolute(arr))