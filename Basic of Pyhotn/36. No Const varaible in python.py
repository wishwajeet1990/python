"""As such python does not have any variable like 
-----------------const---------------------------
as in c,c++,java etc"""

""" # For some reason In large projects, especially with ML, constants are stored in a separate file, like 
# constants.py
PI = 3.14159
MODEL_NAME = "ResNet50"
LEARNING_RATE = 0.001

# main.py
from constants import PI, MODEL_NAME

print(PI)
print(MODEL_NAME)"""


#By convention, we write constants in all UPPERCASE letters. to indicate the developer that the value should not be changed through the programme
# by the way these can be changed 
#for example 

#as per python developer the maker assume that the developer is mature enough that he will not change any such declared variable as in all upper case

PI = 3.14159
GRAVITY = 9.8
APP_NAME = "Wishwajeet AI App"

print(PI)
print(GRAVITY)
print(APP_NAME)


PI = 13.14159
GRAVITY = 99.18
APP_NAME = "Satyajeet AI App"

print(PI)
print(GRAVITY)
print(APP_NAME)
