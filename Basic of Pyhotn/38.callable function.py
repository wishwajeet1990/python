# this piece of code will let you learn the how to check wether the object is callable of non callable 
"""--------------------------Syntax----------------------------
                    callable(object)
            
                return true is the object is callable 
            and return false if the object is not callable
-----------------------------------------------------------------"""
any_num = 12
print(callable(len))        # Return true bcz the built in function of python is callable 
print(callable(any_num))    # this return false bcz it is just a variable 


def greet():
    print("Hello!")
    
print(callable(greet))   # True (it's a function)
print(callable(greet())) # greet() is called first, so result is None; callable(None) False