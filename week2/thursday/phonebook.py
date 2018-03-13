class phonebook(object):
    def __init__(self):
        self.book = "New Phonebook"
        self.entries = {}
    def lookUp(self, name):
        print "%s's number is %s" % (name, self.entries[name])
    def setEntry(self, name, number):
        self.entries[name] = number
        print "Entry stored for %s" % (name)
    def deleteEntry(self, name):
        del self.entries[name]
        print "Entry for %s, deleted." % (name)
    def listAll(self):
        for key, value in self.entries:
            print "%s   :   %s" % (key, value)