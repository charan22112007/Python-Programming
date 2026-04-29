class python:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def op(self):
        print("Student name is : ",self.name)
        print("Studen sem marks in PYTHON : ",self.marks)
s1 = python("Arya",100)
s1.op()