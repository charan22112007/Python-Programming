# Multiple inheritance ==> two or more base/parent classes and one derived/child class
class mother:
    def parent(self):
        print("This is the parent calss...")
class father:
    def parent1(self):
        print("This is the father class...")
class child(mother,father):
    def parentchild(self):
        print("This is from the mother and the father class...")
ch = child()
ch.parentchild()