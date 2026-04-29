numbers = [10,20,30,40]
total = 0
for num in numbers:
    total = total + num
    print("Running Total : ",total)


n = int (input ("How many Numbers? : "))
total = 0
for i in range(n):
    num = int (input("Enter Number : "))
    total += num
    print("Running total : ",total)