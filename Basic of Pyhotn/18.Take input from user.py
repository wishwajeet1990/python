#This programme to used to take input from the user and let store in a variable and access it

print("What is your name ?")
name = input()
age = int(input("what is your age "))

if(age <10 ):
    print(f"Hey ! {name} your age is {age} your are under age to drive the vehicle.")
elif(age>9 and age<18):
    print("Hey ! {} your age is {}. You are are now minor hence you have to first attend the age of 18+ then your are liable to drive vehicle".format(name,age))
elif(age>18 and age<80):
    print("Hey ! %s your age is %d. You are are now adult and your are liable to drive vehicle"%(name,age))
else:
    print("Hey ! %s your age is %d. You are are now overage hence you are not liable to drive vehicle"%(name,age))
    