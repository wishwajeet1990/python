def my_class_decorator(cls):
    cls.greet = "Hello from decorator!"
    return cls

@my_class_decorator
class MyClass:
    pass

obj = MyClass()
print(obj.greet)  # Output: Hello from decorator!