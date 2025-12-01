#Decorator with arguments

# A decorator with arguments is a decorator that itself accepts extra parameters when being applied to a function.

def outer_decorator(arg1, arg2):
# This runs at the moment you APPLY the decorator
    # print(arg1,arg2)
    def actual_decorator(func):
        # This runs every time the decorated function is CALLED
        def wrapper(*args, **kwargs):
            print(f"Decorator args: {arg1}, {arg2}")
            print("Before function runs...")
            func(*args)   # Call original function
            print("After function runs...")
            # return lambda:"nice function"
        return wrapper  #greet = wrapper(greet)
    return actual_decorator # greet = actual_decorator(greet)


@outer_decorator("Hello", "World")
def greet(name):
    print(f"Hi {name}!")

greet("Wishwajeet")
greet("Satyajeet")

# greet = outer_decorator("hello","world")(greet)
# call outer_decorator(arg1,arg2)
# The `# print` statement is a comment in the code. It is not an executable line of code and is used
# to provide a comment or explanation about the code snippet. In this case, it seems like a
# placeholder comment that may have been left for debugging or instructional purposes.
# store arg1  =   "hello" 
# store arg2 = "world"
#return actual_decorator
#so greet = actual_decorator(greet)
#now return wrapper(greet)
    