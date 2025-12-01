#This chapter will make you learn about  how to take input from user
#we take input using input function in python


print("What is your name ?")
name = input()
print("what is your age?")
age = int(input())
if(age <18):
    print(f"Mr {name} your age is {age} . hence you are minor and not liable to drive the vehicle") #using string format
    print("Mr {} your age is {} . hence you are minor and not liable to drive the vehicle".format(name,age)) #using string format function
    print("Mr %s your age is %s . hence you are minor and not liable to drive the vehicle"%(name,age)) #using old style string format
else:
    print(f"Mr {name} your age is {age} . hence you are adult and liable to drive the vehicle") #using string format
    print("Mr {} your age is {} . hence you are minor and not liable to drive the vehicle".format(name,age)) #using string format function
    print("Mr %s your age is %s . hence you are minor and not liable to drive the vehicle"%(name,age)) #using old style string format
    
print("after being update of code runner setting")
