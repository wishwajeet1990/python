# Static methods and class methods in Python help organize code logically inside classes, 
# Static and class method don’t always deal directly with instances. or variable

#Static Method (@staticmethod)
#A regular function that belongs to a class, but it doesn’t use self or cls as an arguments.
#It cannot access or modify instance or class variables.

class calculator:
    name = "Citizen"
    @staticmethod
    def add(a,b):
        calculator.name = "New Cal" #Modifies the class variable from within the static method
                                    # Even though static methods don’t receive self or cls, they can 
                                    # still access the class via the class name directly.            
        print(calculator.name)
        return a+b

c1 = calculator()
print(c1.name)
print(calculator.add(5,7))      #Calling of static method is same as that of regular function
print(c1.name)
#Always calling done via class not by instance

