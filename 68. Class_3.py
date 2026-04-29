class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("My name is : ",self.name)
        print("Age is : ",self.age)
s1 = student("Charan",17)
s1.display()