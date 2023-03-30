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



# Main function defined here #
def main():

    list_1 = [1, 2, 4, 3, 8, 7, 10, 5, 6]

    mx = list_1[0]

    for x in range (len(list_1)):
        if list_1[x] >= mx:

            list_1.append(list_1[x])
            list_1.remove(list_1[x])
            swap_counter =+ 1


    print (list_1)

# Calling the main function #
if (__name__ =="__main__"):
    main()