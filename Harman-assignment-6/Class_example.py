class Animal:
    def __init__(self, name):
        self.name = name

    def intro(self):
        print("Its a ",self.name)

Dog = Animal("DOG")
Cat = Animal("CAT")

# Accessing class methods
Dog.intro()
Cat.intro()