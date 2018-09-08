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

    def birthday(self):
        self.age += 1

# pal is a dog which is a friend to Dog
    def setPal(self, pal):
        self.pal = pal
        pal.pal = self


# Instantiate an object
spotty = Dog("Spotty", 3)
tunker = Dog("Tunker", 10)
harrier = Dog("Harrier", 1)

spotty.setPal(tunker)
# spotty.bark()
# print(spotty.name)


spotty.birthday()
tunker.birthday()


spotty.doginfo()
tunker.doginfo()
harrier.doginfo()

print(spotty.pal.name)
print(spotty.pal.age)

print(tunker.pal.name)
print(tunker.pal.age)
