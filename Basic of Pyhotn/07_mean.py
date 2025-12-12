import numpy as np

my_arr  = np.array([1,2,3,4,5,6,7,8,9,11,20])
sum=0
for i in range(1,np.size(my_arr)):
    print(i,end="")
    sum += my_arr[i]
    print("SUM  = ",sum)
print("Sum  = ",sum)
print("Built in function = ",np.mean(my_arr))
size = np.size(my_arr)
print("Calculated ",sum/size)