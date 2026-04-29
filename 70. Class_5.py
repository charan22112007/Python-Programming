class display:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return "student name is : "+self.name
d1 = display("Charan")
print(d1)

class display:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"student name is {self.name} and age is {self.age}"
d1 = display("Charan",17)
print(d1)