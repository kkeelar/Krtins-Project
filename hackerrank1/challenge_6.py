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

    n1 = input("Please enter how big you would like your X-MAS tree to be minium is 8: ")
    n = int(n1)

    ornament_1 = input ("Please enter the first oranment you would like (Any key works): ")
    ornament_2 = input ("Please enter the seconed ornament: ")
    ornament_3 = input ("Please enter the third ornament: ")
    ornament_4 = input ("Please eneter the fourth ornament: ")

    x = 1
    y = n

    print ((y) * " ", "_")
    print ((y - 1) * " ", "/ \\")
    print ((y - 4) * " ", "---<@>---")
    print ((y - 1) * " ", "\_/")
    print ((y) * " ", "|")

    for i in range(n):

        if (i % 2 == 0):
            print ((y-1) * " ", x * ornament_1, x * ornament_1)

        if (i % 3 == 0):
            print ((y-1) * " ", x * ornament_2, x * ornament_2)


        if (i % 5 == 0):
            print ((y-1) * " ", x * ornament_3, x * ornament_3)

        else:
            print ((y-1) * " ", x * ornament_4, x * ornament_4)


        x = x + 1

        y = y - 1


    for x in range(5):

        print ((n - 1) * " ", "| |")




# Calling the main function #
if (__name__ =="__main__"):
    main()
