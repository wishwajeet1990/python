#Creating the object of class

class emp:
    def __init__(self,name,emp_id,salary):
        self.name = name
        self.empid = emp_id
        self.sal = salary


e1 = object.__new__(emp)                    #create empty object this one need to initialize latter
#or

# e2 = object.__new__(emp,"Wishwajeet singh",213,200000)      #Create an object with default arguments no valid

#or

e2 = emp("Satyajeet Singh",101,200000)      # Same as above declaration of the object of the class but for different object with diff type

#now initialize it(the above object e1)
emp.__init__(e1,"Jhon",200,150000)  # This is same like the object initialization like above statement does 
try:
    e4 = emp()
except Exception as e:
    print("Enter a Valid Name and Emp ID")
    
print("Emp1_ID",e1.empid,"Emp1_NAME",e1.name,"Emp1_ SAL = ",e1.sal)
print("Emp2_ID",e2.empid,"Emp2_NAME",e2.name,"Emp2_ SAL = ",e2.sal)

