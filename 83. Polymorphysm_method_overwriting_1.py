class mother:
    def parent(self):
        print("This is the parent node")
class child(mother):
    def parent(self):
        super().parent()
        print("This is the child class")
ch = child()
ch.parent()