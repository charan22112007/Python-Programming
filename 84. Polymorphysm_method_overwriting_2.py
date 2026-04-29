class animal:
    def sound(self):
        pass
class dog(animal):
    def sound(self):
        super().sound()
        print("Dog bark's")
class cat(animal):
    def sound(self):
        super().sound()
        print("cat meow's")
c = cat()
c.sound()
d = dog()
d.sound()