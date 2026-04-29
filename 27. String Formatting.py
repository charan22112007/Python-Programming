name = "Charan"
age=17
print(f"My name is {name} and I am {age} years old")                # f string function
print("My name is {} and I am {} years old".format(name,age))       # by using format
print("My name is {0} and I am {1} years old".format(name,age))     # by using format
print("My name is {n} and I am {a} years old".format(n=name,a=age)) # by using format
print("My name is %s and I am %d years old" %(name,age))            # by using format specifier