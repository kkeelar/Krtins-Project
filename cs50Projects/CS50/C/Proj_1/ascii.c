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
int reverseElem(int arr[]) {


    int len = sizeof(arr)/sizeof(arr[0]);

    int begin = 0;
    int end = len - 1;
    int place;

    while (begin < end){

        place = arr[begin];
        arr[begin] = arr[end];
        arr[end] = place;
        begin++;
        end--;
    }



    for (int x = 0; x < len; x++){
        printf ("%d \n", arr[x]);
    }



    // Leaves the method and terminates the program
    return 0;

}

int main (void){


    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    reverseElem(arr);

    return 0;
}


