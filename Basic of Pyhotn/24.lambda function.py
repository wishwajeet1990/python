#A lambda is an anonymous function that do not have any name 
#To define an lambda function we use lambda keyword
#it is just used like throughway function that used for just a while 

"""------------------Syntax-----------------------


lambda arguments: expression
Single expression only


----------------------------------------------------"""



square = lambda x : x**2
print(square(5))

"""Here Square is assign the equal functionality as of 

lambda x do have
that mean square is just not work like a normal variable it can accept the argument as well

"""




print("enter your nmber in diffrent sub")
marks = lambda a,b,c,d,e : (a+b+c+d+e)/5
hindi = int(input("hindi :- "))
english = int(input("english :- "))
math = int(input("math :- "))
science = int(input("science :- "))
social_science = int(input("social science :- "))
Average = marks(hindi,english,math,social_science,science)

print("Your Average marks are %d"%Average)
Grade = "A" if Average >=90 else "B" if Average >=80 else "C" if Average>=70 else "D" if Average>=60 else "E"
print("Your Grade is :- %s"%Grade)

if Grade == "A" or Grade=="B" or Grade=="C" or Grade=="D":
   print("Your are Passed Successfully")
else:
    print("You failed")
    