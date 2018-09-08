# oop_py.py
# Create a class named Dog.
# Initialization of that class


class Dog:

    def __init__(self, name, age):  # Add new attributes to object

        self.name = name
        self.age = age


# Instantiate an object
spotty = Dog("Spotty", 3)
print(spotty.name)
print(spotty.age)
