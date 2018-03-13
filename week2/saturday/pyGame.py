from hero import *
from goblin import *
from zombie import *
def main():
    
    while goblin.alive() and hero.alive():
        hero.status()
        goblin.status()
        print
        print "What do you want to do?"
        print "1. fight goblin"
        print "2. do nothing"
        print "3. flee"
        print "> ",
        input = raw_input()
        if input == "1":
            hero.attack(goblin)
        elif input == "2":
            pass
        elif input == "3":
            print "Goodbye."
            break
        else:
            print "Invalid input %r" % input

        if goblin.alive() :
            goblin.attack(hero)

hero = Hero("Hero", 10, 5)
goblin = Zombie("Zombie", 12, 2)
main()