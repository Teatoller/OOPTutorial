# robot_count.py
class Robot(object):
    """docstring for Robot"""

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        """Initialize the data."""
        self.name = name
        print("(Initializing {})".format(self.name))

        # When this person is created, the robot
        # adds to the population

        Robot.population += 1

    def retire(self):
        """ I am taking a break."""
        print("{} is being called back".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                Robot.population))

    def say_hi(self):
        """Greeting by the robot.


        Yes, they can do that."""
        print("Greetings, my masters call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Prints the current population."""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("ChappyR1d1")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("XeroxyR2qd4")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's recall them.")
droid1.retire()
droid2.retire()
