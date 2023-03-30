"""
Krtin Keelar
11/3/2021
AP Comp Sci Princ
6th Period
Basics of Python
"""


# Define the Class; First letter capital in name is Class name, objects have first letter not capital #

class Princess():

     # Intializer #
    def __init__(self, name, numFrogs):
        self.princessName = name
        self.numFrogsKissed = numFrogs

    def getPrincessName(self):
        # This is where user validation goes #
        return self.princessName

    def setPrincessName(self, name):
        # This is where user validation goes #
        self.princessName = name

    def getNumFrogsKissed(self):
        # This is where user validation goes #
        return self.numFrogsKissed

    def setNumFrogsKissed(self, numFrogs):
        # This is where user validation goes #
        self.numFrogsKissed = numFrogs


    def printPrincess(self):
        print ("The princess name is: {0}.".format(self.getPrincessName()))
        print ("She has kissed exactly: {0} frogs.".format(self.getNumFrogsKissed()))