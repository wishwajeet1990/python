#Methods in class are the function class that are bound to the object of the class


class car:
    def __init__(self,make,model,year):
        self.Make = make
        self.Model = model
        self.Year = year
    def display(self):
        print(f"\nThe Make of the car is {self.Make}")
        print(f"The Model of the car is {self.Model}")
        print(f"The Make Year of the car is {self.Year}\n")
        print("The make of the car is {} .\nThe model of the car is {} .\nthe year of manufacturing is {}\n".format(self.Make,self.Model,self.Year))
        print("The make of the car is %s .\nThe model of the car is %s .\nthe year of manufacturing is %d\n"%(self.Make,self.Model,self.Year))

c1 = car("Hyundai","Creta",2019)
print()
print(f"Using object The Make of the car is {c1.Make}")  # Accessing the data member of the class
print(f"Using object The Model of the car is {c1.Model}")    # Accessing the data member of the class
print(f"Using object The Make Year of the car is {c1.Year}") # Accessing the data member of the class

c1.display()        #Accessing the method of the class