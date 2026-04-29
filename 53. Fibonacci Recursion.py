def fibb(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
n = (int(input("Enter number of terms for fibonacci Series : ")))
for i in range(0,n):
    a = fibb(i)
    print(f"{a}",end = "\t")