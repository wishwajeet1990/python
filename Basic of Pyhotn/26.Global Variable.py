Name = "Wishwajeet Singh Tanwar"

def new_function():
    
    # print(Name)     #This will print the global variable name till no variable name will be declared in this function block
    Name = "Satyajeet Singh Tanwar"       #Once the variable name as same as that of the global section the above written statement will gives you an error
    print(Name)   #one the global variable name and local variable name are same and access without the global keyword it will 
    # behave like local variable and print the local variable instead the global one
    
new_function()
