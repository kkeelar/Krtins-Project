/*
Krtin Keelar
12 Aug 2021
Period 6
PSET0
Basics
*/

#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <float.h>

void doSomething();

int main(int agrc, char *argv[]){

    char letter = get_char("Please enter a charecter: ");
    printf ("The charecter you entered is \'%c\'. It's ASCII value is \'%d\' \n\n\n", letter, letter);




    double dub = get_double("Please enter a double: ");
    printf ("The double you entered is \'%e\'. It's ASCII value is \'%d\' \n\n\n", dub, dub);


    float flt = get_float("Please enter a float: ");
    printf ("The charecter you entered is \'%f\'. It's ASCII value is \'%d\' \n\n\n", flt, flt);


    int num = get_int("Please enter an integer: ");
    printf ("The charecter you entered is \'%d\'. It's ASCII value is \'%d\' \n\n\n", num, num);



    return 0;

}


void doSomething(){
    printf("Hello World\n\n\n\n");
}
