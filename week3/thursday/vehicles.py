class Vehicle(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def printInfo(self):
        print self.make
        print self.model
        print self.year