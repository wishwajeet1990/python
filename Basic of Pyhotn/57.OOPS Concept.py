#oops concept in python
#Four Pillars of OOP in Python
"""
    -------------------------------------------------------------------------------------------------------------------------------------
        Concept	                           Description
        Encapsulation	  :-                Hiding internal state and requiring all interaction to be performed through object methods
        Abstraction	      :-                Hiding complex implementation details and exposing only what is necessary
        Inheritance	      :-                Creating a new class from an existing class (reusability of code)
        Polymorphism	  :-                Same method name behaves differently in different classes
    --------------------------------------------------------------------------------------------------------------------------------------
"""


#Simple class
class Dog:
    species = "Canine"
    def __init__(self,Name):
        self.name = Name
    def Speak(self):
        if self.name == "Tommy":
            print(f"{self.name} says woof!")
        else:
            print(f"{self.name} says meaooooo!")
d1 = Dog("Tommy")
d2 = Dog("Catty")

d1.Speak()
d2.Speak()
print(d1.species)
print(d2.species)