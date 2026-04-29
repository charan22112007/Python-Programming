class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name is\t: ",self.name)
        print("Age is\t: ",self.age)
p1 = person("Arya",16)
p1.display()