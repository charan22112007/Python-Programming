n = int(input("Enter a number : "))
temp = n
rev = 0

while temp > 0:
    digit = temp % 10        # get last digit
    rev = rev * 10 + digit   # build reversed number
    temp = temp // 10        # remove last digit

if rev == n:
    print("Palindrome Number")
else:
    print("Not a palindrome Number")