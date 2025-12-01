class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"[INIT] Object {self.name} created.")

    def __del__(self):
        print(f"[DEL] Object {self} is being destroyed.")

obj1 = MyClass("A")
obj2 = MyClass("B")

print(obj1.name)
print(obj2.name)
print("End of program...")

class MyClass2:
    def __init__(self, name):
        self.name = name
        print(f"[INIT] Object {self.name} created.")
    def __del__(self):
        print(f"[DEL] Object {self} is being destroyed.")

obj3 = MyClass2("C")
obj4 = MyClass2("D")
print(obj3.name)
print(obj4.name)
print("End of program...")