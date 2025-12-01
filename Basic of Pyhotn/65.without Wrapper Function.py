# the wrapper function is used because when the we use the decorator function then it runs only once .
# for example 

i = 0


def outer(my_func):
    global i 
    i = i+1
    print("Decorator runs %d"%i)
    return my_func          #Here we return the same function so next time when the decorated function will run
                            # it will be pointing to the self function object and hence no more the 
                            #decorator functionality will takes place and simply run the 
                            # my_func() as usual
                            
@outer
def my_func():
    print("This is my normal function ")

my_func()   #Here when we call the normal function then the decorator will automatically call bcz the function in decorated 
my_func()   #Here no decorator will not runs because no wrapper function is used
my_func()   #Here no decorator will not runs because no wrapper function is used

outer(1)    #Here we are just calling the just a function not the decorator 

"""--------------------output-----------------------------------------
                Decorator runs 1
                This is my normal function
                This is my normal function
                This is my normal function
                Decorator runs 2
-------------------------------------------------------------------------"""

