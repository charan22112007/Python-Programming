# Local Variable
def display():
    a=10
    print("'a' contains : ",a)
display()

# Global Variable
x=10
def display():
    print("'x' contains : ",x,"in display function")
display()
print("Value of 'x' outside the display function : ",x)

y=100
def lvg():
    y=10
    print("Value of local 'y' : ",y)
lvg()
print("Value of Global 'y' : ",y)

# Changining global variable value
z=20
def change():
    global z 
    z = 40
    print(z)
change()
print(z)