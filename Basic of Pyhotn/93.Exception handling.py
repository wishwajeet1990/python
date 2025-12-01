"""
---------------------------------------------what is exception----------------------------------------------
when the programme runs sometimes the error happens like divide by zero, wrong input ,opening a missing file 
these errors are so called exceptions-----------------------------------------------------------------------"""
"""======================what happens id these exception are not taken care======================================
1. the programme got crashed 

Exception are used to take care of smooth continuation of the programme """

"""programme without the exception handling"""

# print(10/0) #ZeroDivisionError: division by zero
# print("End of programme") #This line also be ignored and not printed

try:
    print(10/0)
except ZeroDivisionError:
    print("Can't divide 10 by zero")
    