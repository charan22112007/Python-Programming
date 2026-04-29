#With arguments and with returns
def sum(a,b):
    add = a+b
    return add
a = int(input("Enter 'a' value : " ))
b = int(input("Enter 'b' value : " ))
add = sum(a,b)
print(f"Sum of {a} and {b} is : {add}")