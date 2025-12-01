#Protected Members
#protected member are prefix with one underscore _var.
#Meant to be accessed only inside the class and its subclasses
# Not enforced — you can still access it from outside, but it’s discouraged.

class MyClass:
    def __init__(self):
        self._value = "Protected"

class SubClass(MyClass):
    def show(self):
        print(self._value)  # ✅ Allowed in subclass

obj = SubClass()
print(obj._value)  # ⚠ Possible, but not recommended
print(obj.__dict__)
print(dir(obj))