class Character(object):
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self, enemy):
        # Hero attacks goblin
            enemy.health -= self.power
            print "%s does %d damage to the %s." % (self.name, self.power, enemy.name)
            if enemy.health <= 0:
                print "%s is dead." % enemy.name
    