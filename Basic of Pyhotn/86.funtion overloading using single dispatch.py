#A single dispatch is decorator used in python to make function overloading

#A single dispatch is a function whose behavior depends on the first argument  but only one argument there . Hence is call single dispatch function 

#How it works ?


"""-------------------------------------steps------------------------------------

        1. Decorate defination of the function with singledispatch 
        2. Register the specialized function using .(dot)register(data_type)
        
----------------------------------END-----------------------------------------"""

import functools as fn

@fn.singledispatch
def process_data(data):
    print(f"Default Processing the data : \"{data}\"")

@process_data.register(int)
def __(data):
    print(f"Processing integer value \"{data}\"")    

@process_data.register(str)
def __(data):
    print(f"Processing string value \"{data}\"")

@process_data.register(list)
def __(data):
    print(f"Processing list values \"{data}\"")
my_list = [2,3,4,5,6,7,8,9,10]
my_tuple = (1,2,3,54,6,7,78,191)

process_data("Hello ! Wishwajeet ")
process_data(2)
process_data((2,3,4,5,6,7,8))
process_data(my_list)
process_data(my_tuple)
process_data(2.5)