class Bike:

    def __init__(self,model,color,year):
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
honda=Bike("shine","red","2020")
hero=Bike("splendor","blue","2021")
#hero.getCustomer("Sharat")
print("hero bike details:")
hero.printData()
print("Honda bike details:")

honda.printData()
