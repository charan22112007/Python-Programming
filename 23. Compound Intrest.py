p=float(input("Enter Principle amout : "))
r=float(input("Enter Rate Of intrest : "))
t=float(input("Enter Time (in Years) : "))
amount = p*(1+r/100)**t
ci=amount-p
print("Total amount = ",amount)
print("Compound Intrest = ",ci)