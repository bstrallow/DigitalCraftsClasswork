class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greetCount = 0
        self.peopleGreeted = []

    def __repr__(self):
        return '' % (self.name, self.email, self.phone)

    def greet(self, other_person):
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
        self.greetCount += 1
        for people in self.peopleGreeted:
            if people == other_person:
                print 'Nice to see you again.'
            else:
                self.peopleGreeted.append(other_person)
    def printContact(self):
        print 'You can email me at %s, or call my number %s' % (self.email, self.phone)
    def addFriend(self, newFriend):
        self.friends.append(newFriend)
    def countFriends(self):
        print len(self.friends)
    def peopleMet(self):
        numberMet = len(self.peopleGreeted) - 1
        print numberMet