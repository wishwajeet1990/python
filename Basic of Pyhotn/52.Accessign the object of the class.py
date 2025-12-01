#Accessing the data member of the class

class emp:
    def __init__(self,name,empid,salary):
        self.name = name
        self.emp_id = empid
        self.Sal = salary
        

e1 = object.__new__(emp)
emp.__init__(e1,"wishwajeet singh",213,200000)

# e2 = object.__new__(emp,"Monu",100,250000)    # __New__ Doesn't support any argument except class name
# So when we are declaring the object as __new__ then we need to initialize the separately
e2 = object.__new__(emp)
emp.__init__(e2,"Monu",100,250000)          # Here we initialize the object e2

e3 = emp("Satyajeet Singh",101,200000)
print()
print("Accessing Emp 1 Details")
"""---------------------syntax---------------------------------
            objectname(.dotoperator)data member
--------------------------------------------------------------"""
print("Name :- ",e1.name)
print("Emp ID :- ",e1.emp_id)
print("Salary :- ",e1.Sal)
print()
print("Accessing the Emp2 details")
print("Name :- ",e2.name)
print("Emp ID :- ",e2.emp_id)
print("Salary :- ",e2.Sal)
print()
print("Accessing the Empe3 details")
print("Name :- ",e3.name)
print("Emp ID :- ",e3.emp_id)
print("Salary :- ",e3.Sal)
