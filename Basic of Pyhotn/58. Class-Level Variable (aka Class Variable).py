# Class-Level Variable (Class Variable)

#What it is:

# A variable shared by all objects (instances) of the class.
# Defined outside any methods, but inside the class.
# Belongs to the class, not to any one object.


class Student:
    school_name = "DPS"  # class variable

    def __init__(self, name):
        self.name = name

s1 = Student("Wishwajeet")
s2 = Student("Satyajeet")

print(s1.school_name)  # DPS
print(s2.school_name)  # DPS

Student.school_name = "KVS"  # Changing class variable

print(s1.school_name)  # KVS
print(s2.school_name)  # KVS


#Instance-Level Variable (aka Instance Variable)

#A variable unique to each object (instance).
# Defined using self. inside the __init__ constructor (or any method).
# Belongs to the object, not the class.

class Student:
    def __init__(self, name, roll):
        self.name = name           # instance variable
        self.roll_no = roll        # instance variable
s1 = Student("Wishwajeet", 101)
s2 = Student("Satyajeet", 102)

print(s1.name)      # Wishwajeet
print(s2.name)      # Satyajeet

print(s1.roll_no)   # 101
print(s2.roll_no)   # 102
