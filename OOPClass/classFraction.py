#  classFraction.py
class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, otherfraction):

        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)


myfraction = Fraction(3, 5)

print(myfraction)
print("I ate", myfraction, "of the pizza")
print(myfraction.__str__())
print(str(myfraction))

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)
g = (f1).__add__(f2)
print(g)
