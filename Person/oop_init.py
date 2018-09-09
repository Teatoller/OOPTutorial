# oop_init.py
class Person(object):
    """docstring for Person"""

    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, may name is', self.name)


p = Person('Batman')
p.say_hi()
