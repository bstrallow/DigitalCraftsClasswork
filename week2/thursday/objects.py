class Hello(object):
    def __init__(self):
        self.count = 0
    
    def say_it(self):
        print 'Hello.'
        self.count += 1