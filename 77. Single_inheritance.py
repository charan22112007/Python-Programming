# Single inheritance ==> a child class is derived frokm a parent/existing base class
class A:
    def one(self):
        print("This is the base class...")
class B(A):
    def two(self):
        print("This is the derived class...")
obj=B()
obj.one()
obj.two()