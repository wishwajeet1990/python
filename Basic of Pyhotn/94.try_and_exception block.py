try:                                                    #We will keep such code where the error can be occur
    a = int(input("Enter first number :- "))
    b = int(input("Enter second  number :- "))
    c = a/b
    print(c)
except ValueError:                                      #Handling The error code that may raised during run time
    print("❌ Kindly input a numeric value")
except ZeroDivisionError:                               #Handling The another error code that may raised during run time
    print("❌ Can't Divide by Zero")

finally:                                                #This code will always run 
    print("This is my finally block of exception handling")
print("End of programme")