# The diamond problem occurs in multiple inheritance when a class inherits from
# two classes that both inherit from a common superclass.


        # A
    #    / \
    #   B   C
    #    \ /
        # D
class A:
    def who(self):
        print("A")

class B(A):
    def who(self):
        print("B")

class C(A):
    def who(self):
        print("C")

class D(B, C):  # D inherits from B and C
    pass

d = D()
d.who()  # Output: B
d1 = object.__new__(D)
d1.who()

#Because Python uses something called MRO (Method Resolution Order), and in class D(B, C), it checks: