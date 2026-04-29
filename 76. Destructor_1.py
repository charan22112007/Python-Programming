class person:
    def __init__(self,name):
        self.name = name
        print("Constructor called : ",self.name)
    def __del__(self):
        print("Destructor called : ",self.name)
p1 = person("Hello")
del p1
p1 = person("HI")