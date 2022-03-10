#method overriding

class Birds:
    def fly(self):
        print("all birds fly")
class Eagle(Birds):
    def fly(self):
        super().fly()
        print("eagle flies high")

x=Eagle()
x.fly()


#method overloading  #python does support overloading as it an interpreted language, it only supports overriding
def add(a,b):
    return a+b
def add(a,b,c):     #this is overritten of above one(or this function over writes the previous function
    return a+b+c

#print(add(1,2))    #error is executed
print(add(1,2,3))
