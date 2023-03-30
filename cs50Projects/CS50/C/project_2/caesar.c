
/*
Krtin Keelar
30 Sep 2021
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
#include <ctype.h>


// Main method, takes the number of arguments and provides that there are no parameters taken in this function
int main(int agrc, char *argv[]) {

    // Intilaizes variables for calculations for "encrypting" messages
    // One for upper case, one for lower case, one for non alphabet chareceters
    int calc_for_upper;
    int calc_for_lower;

    // Checks if the amount of arguments given is exactly 2, exits if not so.
    if(agrc!=2){

        // Output message if non integer and exits the program
        printf("Usage: ./casear key\n");
        return 1;
    }

    // Variable and for loop to check if the input is numerical
    string check = argv[1];
    for (int a = 0; a < strlen(check); a++){

        // Checks each charecter in the input to make sure it is an integer
        if (!isdigit(check[a])){

            // Output message if non integer and exits the program
            printf("Usage: ./casear key\n");
            return 1;
        }
    }

    // Creates variables for retrieving the string and the number which we should encrypt by
    string prior = get_string("PLAINTEXT: ");
    int key_value = atoi(argv[1]);


    // Prints the proper prelimenary format for
    printf("ciphertext: ");

    // For loop to calculate the encryption for each letter in the input
    for (int x = 0; x < strlen(prior); x++){

        // Checks if the string input is upper case
        if isupper(prior[x]){

            // Calculates the proper encryption for upper case and prints it
            printf ("%c", ((((prior[x] + key_value) - 65) % 26) + 65));

        }
        // Checks if the string input is lower case
        if islower(prior[x]){

            // Calculates the proper encryption for lower case and prints it
            printf ("%c", ((((prior[x] + key_value) - 97) % 26) + 97));

        }
        // Checks if the string input is a non alphabet charecter
        if (!isalpha(prior[x])) {

            // If not in the alphabet, prints said charecter
            printf("%c", prior[x]);
        }
    }

    // Prints new line
    printf("\n");




    return 0;


}