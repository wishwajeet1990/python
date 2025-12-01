#This programme tell you about the complete else if tutorial

print("What is your name ?")
name = input()
age = int(input("what is your age "))

#Standard format fot if else condition
if(age <10 ):
    print(f"Hey ! {name} your age is {age} your are under age to drive the vehicle.")
elif(age>9 and age<18):
    print("Hey ! {} your age is {}. You are are now minor hence you have to first attend the age of 18+ then your are liable to drive vehicle".format(name,age))
elif(age>18 and age<80):
    print("Hey ! %s your age is %d. You are are now adult and your are liable to drive vehicle"%(name,age))
else:
    print("Hey ! %s your age is %d. You are are now overage hence you are not liable to drive vehicle"%(name,age))
    
#Short hand else if
"""Syntax for shorthand if else"""
# <var> = <true_val> condition else <false_val>

age =int(input("Enter your age "))
print("You are underage") if(age<18) else print("Your are Adult")

#or


status = "underage" if(age<18) else "Adult"
print(f"you are {status}")

# Multilevel Short hand else if

"""Syntax for multilevel if else"""
# <var> = <true_val> condition else <false_val/<True for next elsif>> condition else <false_val>

score = int(input("Input your score "))
grade = "A" if score > 90 else "B" if score > 70 else "C"
print(grade)  

#clever else if 

"""Syntax for clever if else"""
# <var> = (false_val,true_Val) [<condition>]

score = int(input("Input your score "))
grade = ('B','A') [score>70]
print(grade)  
