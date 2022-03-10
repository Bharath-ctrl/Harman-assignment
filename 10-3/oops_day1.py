class Car:
    def __init__(self,model,color,year): #default function
        self.model=model
        self.color=color
        self.year=year

    def printData(self):
        print(self.model)
        print(self.color)
        print(self.year)
    def getCustomer(self,name):
        self.name=name
    def printCustomer(self):
        print(self.name)

benz=Car("3series","black","2020")  #object
bmw=Car("C class","red","2021")
bmw.getCustomer("Bharat")
bmw.printCustomer()


