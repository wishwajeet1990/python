#Private Members
# Prefix with two underscores __var.
# Python performs name mangling: changes __var to _ClassName__var internally.
# This helps avoid accidental overrides in subclasses.
# Still can be accessed, but only with mangled name.

class MyClass:
    def __init__(self):
        self.__secret = "Private"

    def show(self):
        print(self.__secret)

obj = MyClass()
obj.show()  # ✅ Works
# print(obj.__secret)  # ❌ AttributeError
print(obj._MyClass__secret)  # ⚠ Possible but breaking convention


print(obj.__dict__)