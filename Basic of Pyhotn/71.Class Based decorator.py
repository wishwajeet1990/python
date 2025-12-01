#A Class based decorator is the decorator that implemented as class instead a function 


class my_decorator_class:  
    def __init__(self,name):                # This function will be called once when the function is called which is decorated 
        print("Begin __init__ class method")
        self.og_func = name
        self.count = 0
        print("End __init__ class method")
        
    def __call__(self, *args, **kwds):
        print("Begin __Call__ Method of the class")
        result = self.og_func(*args,**kwds)
        self.count+=1
        print("End the __call__ method of the class")
        return result

@my_decorator_class         #when we decorate a function as class based decorator it basically create an 
                            # instance of that class and call init function just once 
                            # then after just calls the __call__function
def greet(name):        
    print(f"hi !{name}")

greet("Wishwajeet")
greet("Monu")
greet("Joni")
greet("Rakhi")
greet("Papa")

print(f"Greet function call : - {greet.count} times")


# @my_decorator_class
# def cal(name):
#     print(f"hi !{name}")
    
    
# cal("Wishwajeet")
# cal("Monu")
# cal("Joni")
# cal("Rakhi")
# cal("Papa")
# cal("toni")

# print(f"Greet function call : - {cal.count} times")
# print()
# print()

# print(f"Greet function call : - {greet.count} times")
# print(f"Greet function call : - {cal.count} times")