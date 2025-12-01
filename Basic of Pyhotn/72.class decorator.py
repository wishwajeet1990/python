# A class decorator is basically a function that accept class as an argument and change the behave
# A class decorator is a function (or another class) that takes a class as input, modifies or enhances it, and returns the same or a new class


def add_prefix(prefix):
    def decorator(cls):
        org_init = cls.__init__
        def new_init(self, *args, **kwargs):
            argv = (prefix + str(args[0]) ,)+ args[1:]
            org_init(self, *argv, **kwargs)
        cls.__init__ = new_init
        return cls
    return decorator

@add_prefix("Mr. ")
class Person:
    def __init__(self, name, age,sex):
        self.name = name
        self.age = age
        self.sex = sex

p = Person("Wishwajeet", 31,"male")
# print(p.age)  # 31
print("Hi",p.name,"Age :-",p.age,"Gender :-",p.sex)  # Hi Mr. Wishwajeet Age :- 31 Gender :- male
print(p.age)  # 31
