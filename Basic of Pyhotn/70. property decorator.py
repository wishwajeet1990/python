
# @property makes your method act like an attribute but still allows you to run custom code when getting, setting, or deleting it.

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        print("Setter Function Run Successfully")
        if value < 0:
            print("You Entered Negative Value to the radius")
            raise ValueError("Negative not accepted")
        else:
            self._radius = value
            
    @radius.deleter
    def radius(self):
        print("Deleting radius...")
        del self._radius
c1 = Circle(3)
# c2 = Circle(-1)
# print(c1.radius)   # getter0
# print(c2.radius)   # getter0
try:
    c1.radius = -8     # setter
except Exception as e:
    print("custom exception Value Can't be negative")
# del c.radius      # deleter
# try :
#     print(c.radius)
# except Exception as e:
#     print("Unable to Print ",e," Because the object has already been deleted before this statement ")
# finally:
#     print("Programme Closed")
