"""
Krtin Keelar
12/10/2021
AP Comp Sci Princ
6th Period
Readability
"""


# Importing necessary libraries; Preprocesser directives
import os, sys
from cs50 import *


# Main function defined here #
def main():

    # Get user input for the text I am going to grade #
    user_text = get_string("Text: ")

    # Variables to hold the number of words, sentences, and letters for the calculations #
    words = 1
    sentences = 0
    letters = 0

    # For loop to count the number of words, sentences, letters #
    for x in range(len(user_text)):

        # Counts number of sentences #
        if ((user_text[x] == "!") or (user_text[x] == "?") or (user_text[x] == ".")):
            sentences += 1

        # Counts number of letters #
        elif (user_text[x].isalpha()):
            letters += 1

        # Counts number of words #
        elif (user_text[x] == " "):
            words += 1

    # Variables for formula; found dependent on relation to 100 word blocks of info #
    L = (letters * (100/words))
    S = (sentences * (100/words))

    # Equation to find the grade of the text #
    grade = (round((0.0588 * L) - (0.296 * S) - 15.8))

    # If statements to accomadate the grade the text is in and prints the proper output #
    if (grade < 1):
        print ("Before Grade 1")
    elif (grade > 16):
        print("Grade 16+")
    else:
        print ("Grade %d" % grade)


# Calling the main function #
if (__name__ =="__main__"):
    main()