#lets have an array
import numpy as np


arr1 = np.array([[1,2,3,4,5,6,7,8,9],[3,54,6,78,9,5,3,2,11]])
arr2 = np.array([[17,55,35,64,53,77,28,93,22],[56,74,68,78,95,54,34,23,33]])

print(np.shape(arr1))
print(np.shape(arr2))
print()
print(arr1)
print()
print(arr2)
print()
print(np.concatenate([arr1,arr2]))  #it return the new array that has all the values that are in arr1 and arr2 but both the array should have same shape