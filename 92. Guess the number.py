class ValueTooSmallError(Exception):
    """Raised when the input value is too small"""
    pass

class ValueToolargeError(Exception):
    """Raised when the imput is too large"""
    pass
number = 10

while True:
    try:
        i_num = int(input("Enter a number : "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueToolargeError
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueToolargeError:
        print("This value is too large, try again!")
        print()

print("Congratulations! You guessed it correctly..")