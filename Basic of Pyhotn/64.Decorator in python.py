#A decorator is powerful feature of the python that allow to modifies or extend the behavior of the function or class without changing their code internally

def deco_func(my_func):         #This is normal function decorator
    print("Hello from deco function")        
    return my_func      #return the same function as it is 

@deco_func      # This takes the next function or class as an argument and pass it to the the decorator function 
def my_normal_function():
    print("this is my normal function")

my_normal_function()