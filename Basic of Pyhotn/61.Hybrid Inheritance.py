#Hybrid Inheritance

class A:
    def feature(self):
        print("Feature from A")

class B(A):
    def feature(self):
        print("Feature from B")

class C(A):
    def feature(self):
        print("Feature from C")

class D(B, C):
    pass


obj = D()
obj.feature()  # Output: Feature from B