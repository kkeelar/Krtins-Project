"""
Krtin Keelar
11/19/2021
AP Comp Sci Princ
6th Period
Basics of Python
"""


# Importing necessary libraries
import os, sys
from cs50 import *


# Main function defined here #
def main():

    # Input for the size of the tree, and converts it to an int #
    input_size = input("Please enter how big you would like your X-MAS tree to be (minimum is 8): ")
    tree_size = int(input_size)

    # Input for the ornaments, or the different charecters on the tree #
    ornament_1 = input ("Please enter the first oranment you would like (Any key works): ")
    ornament_2 = input ("Please enter the seconed ornament: ")
    ornament_3 = input ("Please enter the third ornament: ")

    # Variables for the for loop and for printing the star atop the tree #
    x = 1
    y = tree_size

    # Prints the star at the top of the tree #
    print ((y) * " ", "_")
    print ((y - 1) * " ", "/ \\")
    print ((y - 4) * " ", "---<@>---")
    print ((y - 1) * " ", "\_/")
    print ((y) * " ", "|")


    # For loop creates a tree dependent on the size the user wants #
    for i in range(tree_size):

        # Different rows have different ornaments, this determines where the ornaments go #
        if (i % 2 == 0):
            print ((y-1) * " ", x * ornament_1, x * ornament_1)

        if (i % 3 == 0):
            print ((y-1) * " ", x * ornament_2, x * ornament_2)

        else:
            print ((y-1) * " ", x * ornament_3, x * ornament_3)

        # Iterates through the tree, so it can actually look like a tree #
        x = x + 1
        y = y - 1

    # For loop to create the trunk, dependent on the size of the tree the user wants #
    for x in range(tree_size - 5):
        print ((tree_size - 2) * " ", "|||||")




# Calling the main function #
if (__name__ =="__main__"):
    main()