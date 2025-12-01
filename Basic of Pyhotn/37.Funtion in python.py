""" Syntax of Function Annotation"""

"""----------------------------------------------------------------

    def function_name(param1: type1, param2: type2) -> return_type:
    
    here when we want to tell the user that the particular variable should be of this type but it is not bound to that type of data type
    this hint is written after in parameter
                                          variable : hint type                                   
                                        
And when want to tell the user about the function return type we use simply
                -> hint type

For example

            def function_name(param1: hint type1, param2: hint type2) -> hint return_type:
            
            
--------------------------------------------------------------------"""

#Simple Annotations
def add(a:int,b:int)-> int:
    return a+b

sum = add(2,3)
print(sum)
sum = add(2.98,3.43) # This will also run perfectly fine bcz it doesn't bound to the type of data to passed to a function
print(sum)

# Annotate with Default Values
def greet(name: str = "Friend") -> str:
    return f"Hello, {name}!"
    return str(name)  + "Hello " #This create a misconception while passing an integer through the function 

print(greet())  # This will print the default statement if no parameter is being passed to the function
print(greet(3))  #This will also not bound to the parameter passed to the function and treat it as string value if the the passed arg is not doing any other type(string)of data airthmatic opr


#Using Complex Types (from typing module)
# from typing import List, Dict, Tuple

# def process_data(data: List[int]) -> Tuple[int, int]:
#     return min(data), max(data)


# How to Access Annotations
#this piece of code will let you know the data type hint for parameter and return type hint for the function

def square(n: int) -> int:
    return n * n
print(square.__annotations__) # Output: {'n': <class 'int'>, 'return': <class 'int'>}