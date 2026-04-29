class Car:
    def __init__(self,brand,model,cost,colour):
        self.brand = brand
        self.model = model
        self.cost = cost
        self.colour = colour
    def display(self):
        print("Brand\t: ",self.brand)
        print("Model\t: ",self.model)
        print("Cost\t: ",self.cost)
        print("Colour\t : ",self.colour)
car = Car("RR","Boat Tail","200 crore's","Phantom Black")
car.display()