# Multi level inheritance ==> a child class is derived from another derived class
class A:
    def one(self):
        print("This is the base class...")
class B(A):
    def two(self):
        print("This is the derived class...")
class C(B):
    def three(self):
        print("This is another derived class...")
obj=C()
obj.two()
obj.three()