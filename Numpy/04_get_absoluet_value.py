import numpy as np

arr = np.array([[-1 ,- 7 , 8 , 2 , 3 , 4 , 5],[10 , -70 , 80 , -20 , 30 , -40 , 50],[100 , 700 , -800 , 200 , 300 , -400 , 500]])

#Absolute means the distance between the number from zero without regarding the sign 
print(np.abs(arr))  

print(np.absolute(arr))     #Same as above abs