class person:
    name="Charan Sai Venkata Raju katta"
    age="17"
    def display(self):
        print("Myself ",self.name)
        print(f"I am {self.age} years old")
boy = person()
print(boy.name)
boy.display()