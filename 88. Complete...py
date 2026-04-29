class employee:
    def __init__(self,name):
        self.name = name
    def works(self):
        print("Employee's do the work")
class manager(employee):
    def work(self):
        print(self.name,"The manager manages the team")
class tester(employee):
    def work(self):
        print(self.name,"The tester test's the code")
def employee_details(emp):          # --> common function for all the classes
    emp.work()
m = manager("Girls's")
t = tester("Boy's")
employee_details(m)
employee_details(t)