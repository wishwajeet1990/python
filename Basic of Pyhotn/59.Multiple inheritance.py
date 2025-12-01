#multilevel inheritance

 
class father:
    def house(self):
        print("Father's House")
class Mother:
    def jewelry(self):
        print("Mother's Jewelry")
class Child(father,Mother):
    def car(self):
        print("Child Car")
        
        
c = Child() #Now the child can be able to access the both the class function 


c.house()      # Inherited from Father
c.jewelry()    # Inherited from Mother
c.car()     #Own Method

"""If the derived class is has same method name as that of the base class
 whenever we call the method using the object of the derived class then the latest class function or local class method definition
 will called as per LEGB Rule"""