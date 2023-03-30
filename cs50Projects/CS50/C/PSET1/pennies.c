/*
Erica Wang, Diya Kwerjal, Krtin Keelar
20 Sep 2021
Period 6
PSET1
Pennies
*/
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>


// Main method, takes the number of arguments and provides that there are no parameters taken in this function
int main(int argc, char *argv[]) {

    // Creates the needed variables
    int pennies;
    int days;
    long total;

    //Input number of days in month, makes sure it fits the requirements
    do {
        days = get_int("Days in month: ");
    } while (days < 27 || days > 32);

    //Input number of pennies, makes sure it fits the requirements
    do {
        pennies = get_int("Pennies on first day: ");
    } while (pennies < 1);

    // Sets the intial value
    total = pennies;

    // For loop for calculation
    for(int x = 1; x < days; x++) {

        // Exponential equation, use the power of function
        total = total + pennies * pow(2, x);
    }

    // Gets the final format and adjusts for float math
    double final = (total / 100.0);
    printf("$%.2f\n", final);

    return 0;
}