from character import *
class Hero(Character):
    def status(self):
        print "You have %d health and %d power." % (self.health, self.power)

