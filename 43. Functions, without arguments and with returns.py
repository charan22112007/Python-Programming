#Without arguments and with returns
def sum():
    a = int(input("Enter 'a' value : " ))
    b = int(input("Enter 'b' value : " ))
    add = a+b
    return a,b,add
a,b,add = sum()
print(f"Sum of {a} and {b} is : {add}")