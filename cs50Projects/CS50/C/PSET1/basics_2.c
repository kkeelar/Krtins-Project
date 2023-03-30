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

    float x = FLT_MAX;
    float y = FLT_MIN;

    printf ("The maximun size of Integer is: %.01e. \n", x);
    printf ("The minimum size of Integer is: %.01e. \n", y);

    double a = DBL_MAX;
    double b = DBL_MIN;

    printf ("The maximun size of Integer is: %.01e. \n", a);
    printf ("The minimum size of Integer is: %.01e. \n", b);


    long double j = LDBL_MAX;
    long double k = LDBL_MIN;

    printf ("The maximun size of Integer is: %.01Le. \n", j);
    printf ("The minimum size of Integer is: %.01Le. \n", k);



    printf("The size of float is: %lu\n", sizeof(float));
    printf("The size of double is: %lu\n", sizeof(double));
    printf("The size of long double is: %lu\n", sizeof(long double));

    //Long Starts here
/*
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
*/
    return 0;

}

