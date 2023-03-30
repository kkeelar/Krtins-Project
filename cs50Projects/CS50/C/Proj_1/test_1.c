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


// Main method, takes the number of arguments and provides that there are no parameters taken in this function
int normalizeArr(double arr[], int length) {

    double arr_1[length];

    double place;

    for (int x = 0; x < length; x++){
        place = arr[x] / 6.156;

        arr_1[x] = (place);
    }



    for (int x = 0; x < length; x++){
        printf ("%.3f \n", arr_1[x]);
    }









}


int main(void){


    double arr[] = {2.3, 5.6, -1.1, 0.2};

    int length = sizeof(arr)/sizeof(arr[0]);



    normalizeArr(arr, length);
    return 0;
}
