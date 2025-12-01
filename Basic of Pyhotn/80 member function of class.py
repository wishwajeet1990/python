class MyClass:
    def public_method(self):
        print("Public")

    def _protected_method(self):
        print("Protected")

    def __private_method(self):
        print("Private")

obj = MyClass()
obj.public_method()      # ✅ Allowed
obj._protected_method()  # ⚠ Allowed but discouraged
# obj.__private_method() # ❌ AttributeError
obj._MyClass__private_method()  # ⚠ Possible with name mangling

# Python’s philosophy is "We are all consenting adults here" — 
# it trusts the programmer to respect these conventions instead of enforcing strict access rules.
