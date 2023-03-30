/*
Erica Wang, Diya Kwerjal, Krtin Keelar
21 Sep 2021
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
    long ISBN;
    long value;
    long long array[10] = {};

    // Gets the input, makes sure it fits the requirements
    do {
        ISBN = get_long("ISBN: ");
    } while (ISBN < 0);

    // Splits integer input into an array
    for(int i = 9; i >= 0; i--) {

        // Takes the last digit of the number and assigns it progressing places in the list
        array[i] = ISBN%10;

        // Lowers the number by one place so we can access the next digit in the number
        ISBN = ISBN/10;
    }

    // Calcualtion to determine if the ISBN number is valid by checking each digit by multiplying it by progressing digits.
    value = (1*array[0] + 2*array[1] + 3*array[2] + 4*array[3] + 5*array[4] + 6*array[5] + 7*array[6] + 8*array[7] + 9*array[8]) % 11;



    // If statement used to determine if the ISBN number is valid
    if (value == array[9]) {
        printf("YES\n");
    }  else {
        printf("NO\n");
    }

    return 0;

}