class A:
    def method(self):
        print("This method belongs to Class A")

class B(A):
    def method(self):
        print("Method belongs to b")
class C(A):
    def method(self):
        print("Method belongs to c")

class D(C,B):
    pass

d = D()
d.method()