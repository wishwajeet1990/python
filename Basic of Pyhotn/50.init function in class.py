# __init__() is not mandatory, but very useful.
# If you don’t define it, Python uses the default constructor.
# It always returns None — it’s not for returning data, just for initial setup.

"""
class ClassName:
    def __init__(self, arg1, arg2, ...argn):
        self.attr1 = arg1
        self.attr2 = arg2
        
        
        class ClassName:             Defines a class named ClassName.
        
        def __init__(self, ...)     __init__ is a constructor — automatically called when an object is created.
        
        self    Refers to the current object being created.
        #   Required as the first parameter in all instance methods (including __init__).
        
        arg1, arg2, ... argn            These are parameters passed when the object is created.
        
        self.attr1 = arg1               This creates an attribute for the object and assigns a value from the argument.
        """

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        print("Name = ",self.name)
        print("Name = ",self.roll)

s1 = object.__new__(Student)        #Create new empty object for class student

"""----------Syntax--------------------------
Name_object = object.__new__(class_name)
---------------------------------------------"""
Student.__init__(s1, "Satyajeet", 231)  #Initialized to the data member to these values
"""----------------------------------Another syntax to initialize the data member of the class-------------------------
                    class_name.__init__(object_name,arg1,arg2,....arg_n)
---------------------------------------------------------------------------------------------------------------------"""
#or simply we can use

s1 = Student("Wishwajeet Singh",213)