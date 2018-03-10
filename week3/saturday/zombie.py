from character import *
class Zombie(Character):
    def alive(self):
        if self.health :
            return True
        else:
            return False
    def status(self):
        print "The zombie has %d health and %d power." % (self.health, self.power)
