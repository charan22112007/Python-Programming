# 1. Required arguments
def sum(a,b):
    c = a+b
    print(c)
sum(10,20)
# sum(20,30,40)    --> Gives error

# 2. Default Arguments
def sum(x=10,y=30,z=20):
    add = x+y+z
    print(add)
sum(x=10,y=90,z=20)
sum(x=10)

# 3. Keyword Arguments
        # Identified by the caller of the function 
        # Number of arguments can be taken in any order
def sum(x,y=30,z=40):
    add = x+y+z
    print(add)
sum(10,50,100)
sum(190)

# 4. Variable-Length Arguments / Arbitary Arguments 
def display(*no):
    print(no)
display(10,20,40)

# 5. Positional Arguments
def display(name = "Charan",age = 17):
    print(f'My name is {name} and I am {age} years old')
display()
display("Arya",14)
display(16,"Aegon")
