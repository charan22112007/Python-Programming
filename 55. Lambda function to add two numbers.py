a = int(input("Enter 'a' number : "))
b = int(input("Enter 'b' number : "))
c = lambda a,b : a+b
print(f"The sum of {a} and {b} is : {c(a,b)}")