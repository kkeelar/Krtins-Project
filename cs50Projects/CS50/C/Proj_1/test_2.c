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
int main(void) {


    int date_d1[] = {1, 2, 20};
    int date_d2[] = {0, 10, 15};


    int date_d3[3];
    int len =  sizeof(date_d1)/sizeof(date_d2[0]);

    date_d3[0] = date_d1[0] + date_d2[0];


    if (date_d1[1] + date_d2[1] >= 12){
        date_d3[0] = date_d3[0] + 1;
        date_d3[1] = (date_d1[1] + date_d2[1]) - 12;

    }else{
        date_d3[1] = date_d1[1] + date_d2[1];
    }


    if (date_d1[2] + date_d2[2] >= 30){
        date_d3[1] = date_d3[1] + 1;
        date_d3[2] = (date_d1[2] + date_d2[2]) - 30;
    }else{
        date_d3[2] = date_d1[2] + date_d2[2];
    }




    for (int x = 0; x < len; x++){
        printf ("%d \n", date_d3[x]);
    }




    return 0;

}

