#Let us learn how create custom exception class in python

class my_class(Exception):
    pass

try:
    x = int(input("Enter a number"))
    if x<2:
        raise my_class("Negative number are not allowed")
except my_class as my_cls:
    print("Custom Error",my_cls)
except Exception as e:
    print("Unexpected Error",e)
else:
    print("Number is valid :- ",x)
finally:
    print("Programme Ended")
    