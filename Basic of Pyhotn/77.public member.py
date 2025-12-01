#Public Members
#Default in Python — if you don’t put any underscores, it’s public.
#Accessible from anywhere (inside or outside the class).

class MyClass:
    def __init__(self):
        self.name = "Public"

obj = MyClass()
print(obj.name)  # ✅ Allowed

