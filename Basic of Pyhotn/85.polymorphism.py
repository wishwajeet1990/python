#Polymorphism is comes from latin words in it stand for poly which means many and morphism means form it basic means having more then more 
#than one form is so called polymorphism
#there are two type of polymorphism 
#1. function overloading
#2. operator overloading

# First we will learn function over loading

#polymorphism with function or function overloading

#in python the function overloading works differently it means it choose the correct function at compile time.

#If you had declared the same function with different arguments then the appropriate function will be called 

def greet(name  = "Wishwajeet Singh"):
    print(f"hello ! {name}")

greet()     # this instruction will execute the default parameter function 
greet("Satyajeet Singh")        #In this instruction the the passed parameter will assign to the function 

#conditional based checking function overloading

def cal_area(shape = "ractangale", a = 0 , b = 0):      #here there are three parameter
    if shape == "ractangale":
        area = a*b
        return area
    elif shape == "sqaure":
        area = a*a
        return area
    elif shape == "circle":
        area = 3.14*a*a
        return area

print("Area :- ",cal_area())       #Default parameter will be passed and according area will be printed
print("Area :- ",round(cal_area("circle",3),2))       #Default parameter will be passed and according area will be printed upto 2 decimal points
print("Area :- ",cal_area("sqaure",4))       #Default parameter will be passed and according area will be printed
print("Area :- ",cal_area("ractangale",4,5))       #Default parameter will be passed and according area will be printed
