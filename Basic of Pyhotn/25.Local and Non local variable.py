#A local variable is that which is accessible with in the function block

#A nonlocal variable scope defines that the variable is accessible within the next function in nested function 

# A global scope is that which tell to access the global variable



"""-------------------------------Variable Scope---------------------------
LEGB

L = Local Has more priority if call with the name as declared in global or any other section 
E = Enclosed has more priority after local variable
G = Now the programme gives the 3rd highest priority to the variable called global
B- Finally the programme gives the priority the builtin data type in python

--------------------------------END--------------------------------------------"""


name = "Wishwajeet Singh"   # This variable will accessible within any block 
#whenever you want to chang their value then you need to access it with the prefix global else you can use it 

def outer_function():
    my_outer_string = "Python"
    print(my_outer_string)    
    print(name)
    def inner_function():
        nonlocal my_outer_string    #Here we want to access and assign the values to the variable belong to the just as before the this function outer block 
        global name     #Now we can update the value earlier stored in this variable
        name = "Monu Tanwar"        #Here we had updated
        my_outer_string = "C/C++"       # Here we had assign the new value to the variable
        my_inner_string = "Java"    # this is local variable to the function block
        print(my_inner_string)  
        print(my_outer_string)    
    inner_function()
    # print(my_inner_string)  #In this indentation we cann't access the variable declared in other function block
    print(my_outer_string)
    print(name)     #This is global variable it can be accessed throughout the indentation without being writing the global if the function has no such variable name in it's block
outer_function()
print(name)