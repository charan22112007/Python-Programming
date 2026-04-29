class numdisplay:
    def __init__(self):
        self.x = 100
    def display(self):
        y = 30
        print("Instance variable is : ",self.x)
        print("Normal Variable is : ",y)
n1 = numdisplay()
n1.display()
print("Outside the code Instance Variable is : ",n1.x)
# print(y) ------> Give's Error