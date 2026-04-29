lim = int(input("Enter the limit for the 2 and 3 multiples : "))
for i in range(1,lim+1):
    if i%2==0 or i%3==0:
        print(i)