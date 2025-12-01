"""-----------------------------------------------------in----------------------------------------
in is a keyword in python that is used to check the membership testing and looping of the variable 
--------------------------------------------------------END---------------------------------------"""

if "a" in "apple":       # True, because "a" is in "apple"
    for item in [1, 2, 3]:   # Loops through the list
         print(item)
         
"""--------------------------------------------------is--------------------------------------------------
Tests if two variables refer to the exact same object in memory or we can say to check the object identity
it is Not the same as == which checks for value equality
----------------------------------------------------END--------------------------------------------------"""

a = [1, 2, 3] 
b = a
c = [1, 2, 3]

print("\nExample for is keyword \n")
print("a :- ",a)  # True – same object
print("b :- ",b)  # True – same object
print("c :- ",c)  # True – same object

print("\n")

print("a is b :- ",a is b)  # True – same object
print("a is c :- ",a is c)  # False – different objects with same value
print("a == c :- ",a == c)  # True – values are the same


a = 512215
b = 512215
if a is b:
    print("Value Available")
else:
    print("Value Not available")
    
print("Value of A :- ",a)
print("Value of B :- ",b)
print("Address of A ",id(a))
print("Address of B ",id(b))
print(a is b)           #print true because of constant folding concept in python when a constant have same value then the same 
                        #address space is allocated for best memory optimization
                    
a = "512215"
b = "512215"
print(a is b)           #print false because value is calculated at runtime, Python does NOT intern the number
                    
