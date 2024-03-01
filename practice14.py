class A:
    def method(self):
        print("method of class A")

class B(A):
    def method(self):
        print("method of class B")


class C(A):
    def method(self):
        print("method of class C")

    A.method(0)

class D(B,C):
    pass

d = D()
d.method()



