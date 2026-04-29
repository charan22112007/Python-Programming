a = int(input("Enter 'a' number: "))
b = int(input("Enter 'b' number: "))
max = lambda x,y: f"{x} is big" if x>y else f"{y} ib big"
print(max(a,b))