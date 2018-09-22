#  classFraction.py
class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print(self.num, '/', self.den)


myfraction = Fraction(3, 5)
myfraction.show()
print(myfraction)
