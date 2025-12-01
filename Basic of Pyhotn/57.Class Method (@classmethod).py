# Static methods and class methods in Python help organize code logically inside classes, 
# Static and class method don’t always deal directly with instances. or variable

#Class Method (@classmethod)
#A method that takes cls (the class itself) as its first argument.
#It can access or modify class-level variables, but not instance variables.

class student:
    count = 0       #Class level variable or class level data members
    def __init__(self,name):
        student.name = "Default"     #we need to create class level instance to access it in our @classmethod
        student.count+=1        #we need to create class level instance to access it in our @classmethod
        self.name = name        #Here we are assigning the instance level variable not the class level
        
    @classmethod
    def show(cls):
        print(f"Main Class student Name  = {cls.name}")
        print(f"Total student {cls.count}")     #Accessing the class level variable not the instance level variable
    
        
       

s1 = student("Wishwajeet")  #We are assigning the instance level variable not the class level
s2 = student("Satyajeet")   #We are assigning the instance level variable not the class level

s1.show()         #instance level calling of the variable   . Now the function belong to the class level hence it can access the class level variable not instance level
# s2.show()         #instance level calling of the variable   . Now the function belong to the class level hence it can access the class level variable not instance level

#the above method will not show any name 

# student.name = "Aryan"      #We are trying to assign the class level variable value
# student.show()          #Class level calling of the method