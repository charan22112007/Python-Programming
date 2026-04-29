try:
    # marks = 25
    # result = 25/0
    # print(result)

    # f = open('Stydentregistration','r')
    # print(f.readlines())

    # import add
 
    # list = [1,2,3,4]
    # print(list[7])

    # a = 10
    # b = 20
    # print(a+c)

    # d = int("a") 
    # print(a)

    # a = "aditya"
    # b= 10
    # print(a+b)

    list = {'a':'Aditya','b':'Ball','c':'Canteen'}
    print(list['a'],list['d'])

except ZeroDivisionError:
    print("A number cannot be divided by zero")

except IndexError:
    print("The index is out of range")

except ModuleNotFoundError:
    print("The module named 'add' is not found")

except FileNotFoundError:
    print("The file named 'Stydentregistration' is not found")

except NameError:
    print("The given variable name is not definrd")

except ValueError:
    print("The declared in not of the defined type")

except TypeError:
    print("The declared datatypes does not operate as defined")

except KeyError:
    print("The keyword is not defined")
finally:
    print("Code runs successfully")