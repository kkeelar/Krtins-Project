# Your Agent for solving Raven's Progressive Matrices. You MUST modify this file.
#
# You may also create and submit new files in addition to modifying this file.
#
# Make sure your file retains methods with the signatures:
# def __init__(self)
# def Solve(self,problem)
#
# These methods will be necessary for the project's main method to run.
# Allowable libraries are Python 3.8, Pillow 8.1.0, numpy 1.19.1, and OpenCV4.2.0
# OpenCV 4.2.0, opencv-contrib-python-headless. Non-headless versions of OpenCV will work,
# but the contrib modules of OpenCV like imshow() will not work.

# Install Pillow and uncomment this line to access image processing.
from PIL import Image
import numpy
import cv2

class Agent:
    # The default constructor for your Agent. Make sure to execute any
    # processing necessary before your Agent starts solving problems here.
    #
    # Do not add any variables to this signature; they will not be used by
    # main().
    def __init__(self):
        pass

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    # Remember to return the answer [Key], not the name, as the ANSWERS ARE SHUFFLED.
    # Use var = problem.figures["A"].visualFilename to open files
    # Do not use Absolute pathing to open files.

    def Solve(self,problem):

        #image opt = 1-6, 0 -> 1
        image_opt = [problem.figures["1"].visualFilename,
                     problem.figures["2"].visualFilename,
                     problem.figures["3"].visualFilename,
                     problem.figures["4"].visualFilename,
                     problem.figures["5"].visualFilename,
                     problem.figures["6"].visualFilename
        ]

        im_a = problem.figures["A"].visualFilename
        im_b = problem.figures["B"].visualFilename
        im_c = problem.figures["C"].visualFilename

        return -1
    
    