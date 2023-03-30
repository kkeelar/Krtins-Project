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

int main(int agrc, char *argv[]){

    //Assingments (Sequencing)
    int x = 10;
    x++;
    x+=1;
    x=x+1;
    
    


    //Coditionals (If/Else/Switch)

    if(!(x<12)){
        printf("Tiny little X.");
    } else {
        printf("Bigger X.");
    }


    //Iteration (Looping)
    for (int i=2; i<12; i++){
        printf("%d\n", i)
    }
    
    // Do while
    
    do {
        printf("%d\n", i);
    }while (x<10);
    
    //While do
    
    while (x<10){
        printf("%d\n", i)
    }
    
    return 0;

}

