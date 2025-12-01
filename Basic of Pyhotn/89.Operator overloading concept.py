print("Operator overloading is not possible without making the subclass of the object type")
print("These methods are read-only and can’t be reassigned at runtime.")
# for ex
a = 40
print(a)    #here the print function call the call of type a which is integer type hence it 
            #will call the __str__ of type integer and hence have their own behavior and will print the 
            