class vehicles:
    def move(self):
        print("Vejhicles move")
class car(vehicles):
    def drive(self):
        print("Drive from one palce to another")
class bike(vehicles):
    def ride(self):
        print("Bike's ride")
c = car()
c.drive()
c.move()
b = bike()
b.ride()
b.move()