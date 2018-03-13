from character import *
class Goblin(Character):
    def status(self):
        print "The goblin has %d health and %d power." % (self.health, self.power)
    