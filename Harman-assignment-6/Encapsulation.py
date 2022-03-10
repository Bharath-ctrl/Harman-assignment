class Company:
    def __init__(self):
        self.__salary=50000
    def viewSalary(self):
        print(self.__salary)
    def Manager(self,salary):
        self.__salary=salary

x= Company()
x.viewSalary()

x.__salary=54000
x.viewSalary()

x.Manager(59000)
x.viewSalary()