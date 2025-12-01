#print the function name 
#as ve know in python everything is a class 
#as function is also an object of function class
#hence we call the function name using function_name.__name__ attribute name 

def prefix(func):
    print(f"running {prefix.__name__}")
    def inner(*args ,**kwarg):
        print(f"running {inner.__name__}")
        func()
    return inner

@prefix         #my_func = prefix(my_func)
                #here func = my_func and return new function called inner
                #here in inner function there is command called func.__name__ to print the current function name 
def my_func():
    print(f"Hello from {my_func.__name__}")
    
my_func()
