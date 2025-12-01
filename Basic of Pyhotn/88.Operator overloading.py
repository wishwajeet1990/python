# An operator overloading is to overload the operator to perform different task other then the assign task
#It doesn’t change the operator’s meaning globally — only for your custom class.

#Operator overloading done specially by dunder methods

#Without overloading:

# class student:
#     def __init__(self,name,math,eng,hindi):
#         self.name = name
#         self.math = math
#         self.eng = eng
#         self.hindi = hindi

# s1 = student("Wishwajeet Singh",50,45,66)
# s2 = student("Wishwajeet Singh",50,45,66)

# s3 = s1+s2      #This will raise an error because the operator is used on the operands but not on the objects
# print(s3)

# With overloading
class student:
    def __init__(self,name,math,eng,hindi):
        self.name = name
        self.math = math
        self.eng = eng
        self.hindi = hindi
    def __add__(self,other):
        return student(self.name + " " + other.name , self.math + other.math , self.eng + other.eng , self.hindi + other.hindi)
        
    # def __str__(self):      #this function will take only one arguments 
    #     return f"Person Name = {self.name}\n\nmarks:- \nmath = {self.math} \neng = {self.eng} \nhindi = {self.hindi}\n\n"
    
s1 = student("Wishwajeet Singh",50,45,66)
s2 = student("Satyajeet Singh",50,45,66)

s3 = s1+s2      #This will raise an error because the operator is used on the operands but not on the objects if no operator overloading 
                #defination is not done 
print(s1)
print(s2)
print(s3)

print(str(s1),str(s2))  #This print statements do have argument and we want supposed to print 
                        # both of these then we have to pass it to str function instead of direct passing
