#this programme will let you know about the classes 

#A class is blueprint of data and method together 

# Every method is a function,
# But not every function is a method.

# A function is a reusable block of code that can be called independently, without being tied to an object
# A method is a function that is bound to an object (like a string, list, class instance, etc.).

class RT_Vision:
    #Data member of the class that hold the data  
    name = "Wishwajeet"
    emp_id = "RTV213"
    
    # This is a special function of the class that is used to initialize the default value to the data member of the class
    #this invoked automatically whenever the object of the class is created 
    #if you create n number of object then it will called each time and assign the default values to the data member of the class 
    
    def __init__(self,name  = "Wishwajeet",emp_id = "RTV213"):
        self.name = name
        self.emp_id = emp_id
        print(f"name :- {self.name}",f"Emp Id :- {self.emp_id}")

rtv_1 = RT_Vision()     #Constructor will automatically be called
rtv_2 = RT_Vision("Satyajeet","RTV222")     #Constructor will automatically be called
rtv_3 = RT_Vision()     #Constructor will automatically be called
rtv_4 = RT_Vision()     #Constructor will automatically be called
rtv_5 = RT_Vision()     #Constructor will automatically be called