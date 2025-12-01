#create object in class

class test_class:
    def __init__(self,name,age,sex,exp):
        self.name = name
        self.age=age
        self.sex = sex
        self.exp=exp


t1 = object.__new__(test_class)
test_class.__init__(t1,"wishwajeet",34,"M","6 Yrs")
print()
print("Fetch the data")
print("Name :- ",t1.name)
print("Age :- ",t1.age)
print("Sex :- ",t1.sex)
print("Experience :- ",t1.exp)
