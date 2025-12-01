#This programme will let yoy know about the constructor 

class student:
    
    def __init__(self, name,emp_id):
        self.name = name
        self.emp_id = emp_id
        self.salary = None      #we want this attribute or data member to be exits but this is not a part of our default constructor this can be initialized latter separately 
                                #without pass while creating  the object of the class
        
        print("Default values assign to the following using constructor")
        print("Name = ",self.name)
        print("Emp_Id = ",self.emp_id)
        print("Salary = ",self.salary)

s1 = student("Wishwajeet Singh","RTV213")     # default values to the class members
s1.salary= 200000           #This is initialized latter hence during constructor it will no be initialized 
print()
print("Accessing the data member of the class")
print("Name = ",s1.name)      #when to access the member of the class use object of that class followed by (.) operator with attribute
print("Emp_Id = ",s1.emp_id)    #when to access the member of the class use object of that class followed by (.) operator with attribute
print("Salary = ",s1.salary)    #when to access the member of the class use object of that class followed by (.) operator with attribute
