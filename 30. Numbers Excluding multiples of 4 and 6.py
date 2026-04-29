lim = int(input("Enter the limit of the numbers : "))
for i in range(1,lim+1):
    if i%4==0 or i%6==0:
        continue
    print(i)