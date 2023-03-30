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

int main(int agrc, char *argv[]){

   // printf("ArgC is: %s. \n\n", argc"):

    //for (int i = 0; i < argv; i++){
       // printf("Argv[%d] is %s. \n", i, argv[i]);
    //}

    int randomNumber;
    bool done = true;

    do {
            srand(time(NULL));
            randomNumber = rand() % 10;
            //Seeding the random number generator
            //Our first loop
            if (randomNumber % 2 == 0) {
                printf("The number is %d, which is EVEN\n", randomNumber);
            } else {
                printf("The number is %d, which is ODD\n", randomNumber);

            }

            switch(randomNumber){
                    case 1: printf("The number is one\n");
                            break;
                    case 2: printf("The number is two\n");
                            break;
                    case 4: printf("The number is four\n");
                            break;
                    case 6: printf("The number is six\n");
                            done = true;
                            break;
                    default: printf("This something else\n");



            }


        //Closing while loop

    }  while(!done);







     //for-loop practice



    int arr[5] = {55, 49, 17, 9, 16};




    for (int x = 0, y = (sizeof(arr)/sizeof(int)); x < y; x++){
        printf("%d \n", arr[x]);
    }



    printf("\n");
    for (int x = (sizeof(arr)/sizeof(int))-2, y = 0; x>=y;x-=2 ){
        printf("%d \n", arr[x]);
    }

    return 0;

}

