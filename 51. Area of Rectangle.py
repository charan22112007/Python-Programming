# Area of rectangle
def main():
    l,b = get_values()
    area = cal_area(l,b)
    display(area)
def get_values():
    return int(input("Enter length : ")),int(input("Enter Breadth : "))
def cal_area(l,b):
    return l*b
def display(area):
    print("The area is : ",area)
main()