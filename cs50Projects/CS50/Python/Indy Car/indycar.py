"""
Krtin Keelar
11/14/2021
AP Comp Sci Princ
6th Period
Basics of Python
"""


# Define the Class; First letter capital in name is Class name, objects have first letter not capital #


class IndyCar():

    # Intializer #
    def __init__(self, carType, fuel, bestLapSpeed, avgLapSpeed, numOfTires, carCost):
        self.fuel = fuel
        self.bestLapSpeed = bestLapSpeed
        self.avgLapSpeed = avgLapSpeed
        self.numOfTires = numOfTires
        self.carType = carType
        self.carCost = carCost

    # Getter and setter for fuel #
    def getFuel(self):
        return self.fuel
    def setFuel(self, fuel):
        self.fuel = fuel

    # Getter and setter for best lap speed #
    def getBestLapSpeed(self):
        return self.bestLapSpeed
    def setBestLapSpeed(self, bestLapSpeed):
        self.avgLapSpeed = bestLapSpeed

    # Getter and setter for average lap speed #
    def getAvgLapSpeed(self):
        return self.avgLapSpeed
    def setAvgLapSpeed(self, avgLapSped):
        self.avgLapSpeed = avgLapSpeed

    # Getter and setter for the number of tires #
    def getNumOfTires(self):
        return self.numOfTires
    def setNumOfTires(self, numOfTries):
        self.numOfTires = numOfTires

    # Getter and setter for the car type #
    def getCarType(self):
        return self.carType
    def setCarType(self, carType):
        self.carType = carType

    # Getter and setter for the car cost #
    def getCarCost(self):
        return self.carCost
    def setCarCost(self, carCost):
        self.carCost = carCost


    # Function to determine the overall score of the cars #
    def carScore(self, avgLapSpeed, fuel, numOfTires, bestLapSpeed):
        score = ((avgLapSpeed * 100) - ((fuel + numOfTires) * 10)) + bestLapSpeed
        return (score)

    # Function to determine the effiecney of the cars #
    def carEfficeney(self, avgLapSpeed, fuel):
        efficeney = (avgLapSpeed / fuel)
        return (efficeney)

    # Function to determine the best budgeted car #
    def bestBudget(self, avgLapSpeed, fuel, numOfTires, carCost, bestLapSpeed):
        score = ((avgLapSpeed * 100) - ((fuel + numOfTires) * 10)) + bestLapSpeed
        budget = score / carCost
        return (budget)

    # Procedure to print all of the car's information
    def printCar(self):
        #print ("The score : {0}.".format(self.carScore(self.avgLapSpeed, self.fuel, self.numOfTires)))
        print ("The fuel in pounds burned per lap is: {0}.".format(self.getFuel()))
        print ("The car's best lap speed is: {0}".format(self.getBestLapSpeed()))
        print ("The car's average lap speed for a 100 laps is: {0}".format(self.getAvgLapSpeed()))
        print ("The car burned through this many tires in 100 laps: {0}".format(self.getNumOfTires()))
        print ("The car's cost is: {0}".format(self.getCarCost()))