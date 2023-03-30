
/*
Krtin Keelar
18 Oct 2021
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


// Main method, takes the number of arguments
int main(int agrc, char *argv[]) {

    // Intilaizes variables for calculations for "encrypting" messages
    // One for upper case, one for lower case, one for non alphabet chareceters
    int calc_for_upper;
    int calc_for_lower;

    // Checks if the amount of arguments is exactly 2, exits if not so.
    if(agrc!=2){

        // Output message if non integer and exits the program
        printf("Usage: ./vigenere key\n");
        return 1;
    }


    // Intiliazies variables dependent on the user input
    // Used in the for loops
    string check = argv[1];
    int input_len = strlen(check);

    // For loop to check the proper inputs are given
    for (int a = 0; a < strlen(check); a++){

        // Checks each charecter in the input to make sure it is in the alphabet
        if (!isalpha(check[a])){

            // Output message if not in the alphabet and exits the program
            printf("Usage: ./vigenere key\n");
            return 1;
        }
    }

    // Creates variables for retrieving the string and prints the format for the final output
    string prior = get_string("PLAINTEXT: ");
    printf ("ciphertext: ");

    for (int x = 0, z = 0, check_1 = strlen(prior); x < check_1; x++){

        // Creates the proper key for encryption, and checks through each input for encyrption
        int key = tolower(check[z % input_len]) - 97;

        // Checks if the string input is upper case
        if isupper(prior[x]){

            // Calculates the proper encryption for upper case and then prints it
            // Increases the z value, checking the next input charecter to encyrpt by
            calc_for_upper = (65 + (prior[x] - 65 + key) % 26);
            printf ("%c", calc_for_upper);
            z++;
        }
        // Checks if the string input is lower case
        else if islower(prior[x]){

            // Calculates the proper encryption for lower case and prints it
            // Increases the z value, checking the next input charecter to encyrpt by
            calc_for_lower = (97 + (prior[x] - 97 + key) % 26);
            printf("%c", calc_for_lower);
            z++;
        }
        // Checks if the string input is a non alphabet charecter
        else if (!isalpha(prior[x])) {

            // If not in the alphabet, just prints said charecter
            printf("%c", prior[x]);
        }
    }

    // Prints new line
    printf("\n");



    return 0;


}