# oop_py.py
# Create a class named Dog.
# Initialization of that class


class Dog:

    def __init__(self, name, age):  # Add new attributes to object

        self.name = name
        self.age = age

# Define method in class
    def bark(self):
        print("Woof, woof!")

    def doginfo(self):
        print(self.name + " is " + str(self.age) + " year(s) old")
        print(self.bark())


# Instantiate an object
spotty = Dog("Spotty", 3)
tunker = Dog("Tunker", 10)
harrier = Dog("Harrier", 1)
# spotty.bark()
# print(spotty.name)
# print(spotty.age)

spotty.doginfo()
tunker.doginfo()
harrier.doginfo()
