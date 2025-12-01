#method resolution order is the process of how the order methods or accessing attributes in which Python will search classes when executing methods or accessing attributes.
class A:
    def show(self):
        print("Class A")
        pass

class B(A):
    def show(self):
        print("Class B")
        pass

class C(A):
    def show(self):
        print("Class C")
        pass

class D(B, C):
    #in this case when the object is created then when we call the show function it will firstly search for the show function in itself class
    # the it will search at the order in which the parent class are passed to child class as a object while declaring the child class
    # here B is passed as first argument the c is passed as second argument 
    #hence when the object of this class will be created it will search for show function in d class then in b then in c
    # def show(self):
    #     print("Class D")
        pass

# Print MRO
# print(D.__mro__)
print(D.mro())

d1 = D()
d1.show()
