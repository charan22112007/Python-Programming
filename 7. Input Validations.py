# Type validation
age=input("Enter age")
if age.isdigit():
    age = int(age)
    print("Valid Age")
else:
    print("Invalid Age")
# range validation
n=int(input("Enter a number"))
if 1<n<10:
    print("Valid")
else:
    print("Invalid")
# Size/Length validation
p=input("Enter Passord")
if len(p)>=6:
    print("strong")
else:
    print("Too Week")
# Format validation
email=input("Enter mail")
if '@' in email and '.' in email:
    print("Valid mail")
else:
    print("invalid mail")