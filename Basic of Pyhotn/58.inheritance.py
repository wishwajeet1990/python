#Inheritance is an oops concept that are used to derive a new class using existing class
"""
| Type            | Description                                                   |
| --------------- | ------------------------------------------------------------- |
| Multilevel      | Chain of inheritance (A → B → C)                              |
| Multiple        | A class inherits from multiple classes                        |
| Hybrid          | Mix of multi-level and multiple                               |
| Diamond Problem | Two child inherit from same parent class, child inherits from both |

"""

class Father:
    def house(self):
        print("Father's House")

class Mother:
    def jewelry(self):
        print("Mother's Jewelry")

class Child(Father, Mother):        #Inherited from the father and mother
    #--------------------syntax----------------------
    
    # class class_name(base_class1,base_class2,....base_class_name_n):
    
    # -----------------------------------------------------------------
    pass

c = Child()
c.house()      # Inherited from Father
c.jewelry()    # Inherited from Mother


