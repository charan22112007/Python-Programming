def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
n = (int(input("Enter a number for factorial : ")))
print(f"The factorial of {n} is : {fact(n)}")