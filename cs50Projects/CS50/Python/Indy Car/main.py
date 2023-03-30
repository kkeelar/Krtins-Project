"""
Krtin Keelar
11/14/2021
AP Comp Sci Princ
6th Period
Basics of Python
"""


# Importing necessary libraries
import os, sys
from cs50 import *
from indycar import IndyCar



# Main function defined here #
def main():

    # Creates lists to determine the best cars
    scorer = []
    effciencey = []
    best_budget = []

    # Each chunk of code prints or gathers specific functions from the class #
    print ("This is Car 1's information")
    car_1 = IndyCar("Mercedes", 60, 200, 125, 16, 72000)
    car_1.printCar()
    print("This is the car type", car_1.getCarType())
    scorer.append(car_1.carScore(125, 60, 16, 200))
    effciencey.append(car_1.carEfficeney(125, 60))
    best_budget.append(car_1.bestBudget(125, 60, 16, 72000, 200))

    print ("\n")

    # Each chunk of code prints or gathers specific functions from the class #
    print ("This is Car 2's information")
    car_2 = IndyCar("Porsche", 64, 221, 125, 24, 63000)
    car_2.printCar()
    print("This is the car type", car_2.getCarType())
    scorer.append(car_2.carScore(125, 64, 24, 221))
    effciencey.append(car_1.carEfficeney(125, 64))
    best_budget.append(car_1.bestBudget(125, 64, 24, 63000, 221))

    print ("\n")

    # Each chunk of code prints or gathers specific functions from the class #
    print ("This is Car 3's information")
    car_3 = IndyCar("BMW", 64, 231, 142, 14, 87200)
    car_3.printCar()
    print("This is the car type", car_3.getCarType())
    scorer.append(car_3.carScore(142, 64, 14, 231))
    effciencey.append(car_1.carEfficeney(142, 64))
    best_budget.append(car_1.bestBudget(142, 64, 14, 87200, 231))

    # Finds the best cars in different categories #
    max_score = (max(scorer))
    max_eff = (max(effciencey))
    final_bb = (max(best_budget))

    best_car = scorer.index(max_score)
    best_eff = effciencey.index(max_eff)
    best_bb = best_budget.index(final_bb)



    # Prints our final scores on which car is the best in each area #
    print ("\n")
    print ("Car %d scored the best and was the best overall car" % (best_car + 1))
    print ("Car %d was the most efficent in terms of fuel consumption" % (best_eff + 1))
    print ("Car %d did the most with the least amount of money" % (best_bb + 1))







# Calling the main function #
if (__name__ =="__main__"):
    main()