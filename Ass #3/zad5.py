class Bug:
    ''' Bug class that counts all class instances'''

    conter = 0

    def __init__(self):
        Bug.conter += 1
        self.id = Bug.conter

    def __del__(self):
        Bug.conter -= 1
        print(" End ID = " + str(self.id) + ", Counter: " + str(Bug.conter))

    def __str__(self):
        return " End ID = " + str(self.id) + ", Counter: " + str(Bug.conter)

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])