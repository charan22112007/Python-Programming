lim = int(input("Enter the limit for Fibonacci series : "))
f = 0
num = 1

print("Fibonacci Series:")

for i in range(1,lim+1):
    print(f, end=" ")
    t = f + num
    f = num
    num = t