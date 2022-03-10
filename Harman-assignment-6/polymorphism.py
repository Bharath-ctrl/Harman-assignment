class Flight:
    def fly(self):
        print("all flights fly")
    def size(self):
        print("Most of the flights are big.")
class Antonov(Flight):
    def size(self):
        super().size()
        print("Antonov was the biggest airplane")



x=Antonov()
x.size()
