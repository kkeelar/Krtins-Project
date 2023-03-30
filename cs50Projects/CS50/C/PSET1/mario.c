/*
Group E: Diya Kejriwal, Erica Wang, Krtin Keelar
14 Sep 2021
Period 6
PSET1
Mario Project
*/
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <float.h>

// Main method, takes the number of arguments and provides that there are no parameters taken in this function
int main(int argc, char *argv[]){

    int height;

    // Gets the height input, makes sure the height fits the requirements
    do {
        height = get_int("Height: ");
    } while (height < 1 || height > 8);

    // For loop to print the entire staircase as a whole
    for(int x = 1; x <= height; x++) {

        // Prints the spaces before first staircase
        for(int i = 0; i < (height - x); i++) {
            printf(" ");
        }

        // Prints the first side of staircase
        for(int i = 0; i < x; i++) {
            printf("#");
        }

        // Prints the gap in between staircases
        printf("  ");

        // Prints the opposing side of staircase
        for(int i = 0; i < x; i++) {
            printf("#");
        }

        //Prints new line
        printf("\n");
    }



    return 0;
}
