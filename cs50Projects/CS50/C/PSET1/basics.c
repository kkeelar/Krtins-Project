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

    int x = INT_MAX;
    int y = INT_MIN;

    printf ("The maximun size of Integer is: %d. \n", x);
    printf ("The minimum size of Integer is: %d. \n", y);

    unsigned int z = UINT_MAX;

    printf ("The maximun size of unsigned Integer is: %d. \n", z);

    //Long Starts here

    long a = LONG_MAX;
    long b = LONG_MIN;

    printf ("The maximun size of Long is: %ld. \n", a);
    printf ("The minimum size of Long is: %ld. \n", b);

    unsigned long c = ULONG_MAX;

    printf ("The maximun size of Integer is: %lu. \n", c);

    long j = LLONG_MAX;
    long k = LLONG_MIN;

    printf ("The maximun size of Long is: %ld. \n", j);
    printf ("The minimum size of Long is: %ld. \n", k);

    unsigned long long l = ULLONG_MAX;

    printf ("The maximun size of Integer is: %llu. \n", l);



    printf("The size of integer is: %lu\n", sizeof(int));
    printf("The size of integer is: %lu\n", sizeof(long));
    printf("The size of integer is: %lu\n", sizeof(long long));

    return 0;

}

