import numpy as np
my_arr = np.arange(1,1000000001,dtype=np.int32)
print("Before Reshape")
print(my_arr)

new_array = my_arr.reshape(100,10000000)
print("After Reshape and save to new array")
print(new_array)
