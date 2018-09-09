# oop_sample.py
class pet(object):
    """docstring for pet"""
    number_of_legs = 0

    def sleep(self):
        print "zzz"


flaffy = pet()
flaffy.sleep()
flaffy.number_of_legs = 4
print "Flaffy has %s legs." % flaffy.number_of_legs
print('Flaffy has {} legs.').format(flaffy.number_of_legs)
