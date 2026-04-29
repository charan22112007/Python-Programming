# Hybrid Inheritance ==> a class is derived from two or more already derived classes
class animal:
    def sound(self):
        print("Animals make sounds")
class mammal(animal):
    def make_sound(self):
        print("Mammals make sound")
class bird(animal):
    def makes_sound(self):
        print("Birds make sound")
class bat(mammal,bird):
    pass
obj=bat()
obj.make_sound()
obj.makes_sound()
obj.sound()