#Without default constructor

class student:
    name = None
    roll_no= None
    class_n = None

#Wrong practice because the default constructor is not taking any other argument other than self
s1 = object.__new__(student)
# student.__init__(s1,"Wishwajeet Singh",101,"5th")

s2 = student()
s2.name = "Wishwajet Singh"
s2.roll_no = 101
s2.class_n = "5th"

"""Due to wrongly initialize the data member you can't access these data member as well """

print("Accessing the Data member of the class student using s1 object ")
print("Name :- ",s1.name)
print("Roll No :- ",s1.roll_no)
print("Class :- ",s1.class_n)

print("Accessing the Data member of the class student using s2 object ")
print("Name :- ",s2.name)
print("Roll No :- ",s2.roll_no)
print("Class :- ",s2.class_n)