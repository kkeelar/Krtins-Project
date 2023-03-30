"""
Krtin Keelar
11/3/2021
AP Comp Sci Princ
6th Period
Basics of Python
"""


# Importing necessary libraries
import os, sys
from cs50 import *
from princess_class import Princess


# Main function defined here #
def main():

    # Passes arguments to an object, the object is princessOfTheDay #
    princessOfTheDay = Princess("Cinderella", 5)

    # Calls the printPrincess function from the class with the parameters outlined above, this is done by using the object #
    princessOfTheDay.printPrincess()

    # Passes a different number of frogs kissed to the setNumFrogsKissed function, then prin the new info #
    princessOfTheDay.setNumFrogsKissed(2145)
    princessOfTheDay.printPrincess()

    # Calls just the get princess name function, prints it with the parameters above and again uses the object decalred above #
    print (princessOfTheDay.getPrincessName().upper())
    print (princessOfTheDay.getPrincessName().lower())
    princessOfTheDay.setNumFrogsKissed(-4354)




# Calling the main function #
if (__name__ =="__main__"):
    main()