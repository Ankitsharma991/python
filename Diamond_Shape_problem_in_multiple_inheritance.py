class A:
    def met(self):
        print("This is a method from class A")

class B(A):
    def met(self):
        print("This is a method from class B")

class C(A):
    def met(self):
        print("This is a method from class C")

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

d.met()