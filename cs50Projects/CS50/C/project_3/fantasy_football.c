/*
Krtin Keelar
29 Oct 2021
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
#include <curl/curl.h>


string player_1_name(){

    printf ("\nWelcome to the fantasy assistant \n");
    printf ("\nWe know picking a week to week starter is hard, so we're gonna help you out \n");
    printf ("\nJust enter the two players you want to compare like this (patrick-mahomes-ii)  \n");

    string P1_name = get_string("Enter Player 1: ");
    return P1_name;
}


string player_2_name(){

    string P2 = get_string("Enter Player 2: ");
    return P2;
}

void data_1(string P1) {
    char first_url[100];
    strcpy(first_url, "https://www.foxsports.com/nfl/");
    strcpy(first_url, "lamar-jackson-player");
    printf("FIRST URL %s\n", first_url);
    

    //return first_url;
}

char * data_2(string P2) {

    char *sec_url = malloc(31);
    //char * sec_url = (char *)malloc(sizeof(char) * 50);
    sec_url = "https://www.foxsports.com/nfl/";
    char player_2[strlen(P2)];
    for (int y = 0; y < strlen(P2); y++){
        player_2[y] = P2[y];
    }

    printf("%s", player_2);
    player_2[strlen(P2)] = '\0';
    char add_on[] = "-player";
    strcat(sec_url, player_2);
    strcat(sec_url, add_on);
    printf ("this is P2 url %s \n", sec_url);
    //sec_url[strlen(sec_url)] = '\0';
    return sec_url;
}

// Main method, takes the number of arguments
int main(int agrc, char *argv[]) {

    string P1 = player_1_name();

    string P2 = player_2_name();

    printf("this is HHHH P1:%s \n", P1);
    printf("THis iis HHHHHH P2: %s \n", P2);

    data_1(P1);

    // final_url_1 = data_1(P1);

    string final_url_2 = data_2(P2);

    /*
    printf("Url: %s \n", final_url_1);
    printf("Url_2: %s \n", final_url_2);
    printf("P2: %s \n", P1);
    printf("P1: %s \n", P2);
    */



    /* Prints new line */
    printf("\n");

    /* Intilizaes the libray, finds the proper URL to pull from, and writes the data into a file with a call back function */
    CURL *curl = curl_easy_init();
    curl_easy_setopt(curl, CURLOPT_URL, final_url_1);
    /* Writes the data into the proper file */
    FILE * f_1;
    f_1 = fopen("player_1_info.txt", "wb");
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, f_1);
    /* Retrieves the proper data, if issue in pulling data, tells user */
    curl_easy_perform(curl);
    /* Proper clean up */
    fclose(f_1);
    curl_easy_cleanup(curl);

    /* Process of gathering and displaying data */
    /* Opens file in proper mode creates needed variables for displaying and comparing data, all creates the XPATH where the data I am looking for is stored */
    FILE * check_f_1;
    check_f_1 = fopen("player_1_info.txt", "r");
    string check = "<span class=\"fs-23 cl-wht\">";
    char line[10000], nextPartLine[1000], final_line[1000];
    char* yards_p1 = (char *)malloc(sizeof(char) * 5);
    char* tds_p1 = (char *)malloc(sizeof(char) * 5);
    char* ints_p1 = (char *)malloc(sizeof(char) * 5);
        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line, sizeof(line), check_f_1) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line, check) != NULL){
                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result = strstr(line, check);
                int position = result - line + strlen(check);
                printf ("Player 1 yards: ");
                for (int i = position, x = 0; i < position + 4; i++, x++) {
                    if (isdigit(line[i])){
                        printf("%c", line[i]);
                        yards_p1[x] = line[i];
                    }
                }
                /* All three data points I am looking for are on the same line in the HTML file, so I create a new line on which I look for the next and then the final data I need */
                for(int k = 0,  j = position + strlen(check); j < sizeof(line) ; j++, k++) {
                    nextPartLine[k] = line[j];
                }
            /* Follows same process as above */
            if (strstr(nextPartLine, check) != NULL){
                char* result_1 = strstr(nextPartLine, check);
                int position_1 = result_1 - nextPartLine + strlen(check);
                printf ("Player 1 touchdowns: ");
                for (int i = position_1, x = 0; i < position_1 + 2; i++, x++) {
                    if (isdigit(nextPartLine[i])){
                        printf("%c", nextPartLine[i]);
                        tds_p1[x] = nextPartLine[i];
                    }
                }
            for(int k = 0,  j = position_1 + strlen(check); j < sizeof(line) ; j++, k++) {
                    final_line[k] = nextPartLine[j];
                }
            }
            /* Follows same process as above */
            if (strstr(final_line, check) != NULL){
                char* result_2 = strstr(final_line, check);
                int position_2 = result_2 - final_line + strlen(check);
                printf ("Player 1 interceptions: ");
                for (int i = position_2, x = 0; i < position_2 + 1; i++, x++) {
                    if (isdigit(final_line[i])){
                        printf("%c \n", final_line[i]);
                        ints_p1[x] = final_line[i];
                    }
                }
            }

            }
        }

        /* Prints new line */
        printf ("\n");

        /* Intilizaes the libray, finds the proper URL to pull from, and writes the data into a file with a call back function */
        CURL *curl_1 = curl_easy_init();
        curl_easy_setopt(curl_1, CURLOPT_URL, final_url_2);
        /* Writes data into the proper file */
        FILE * f_2;
        f_2 = fopen("player_2_info.txt", "wb");
        curl_easy_setopt(curl_1, CURLOPT_WRITEDATA, f_2);
        curl_easy_perform(curl_1);
        /* Clean up */
        fclose(f_2);
        curl_easy_cleanup(curl_1);

        /* Process of gathering and displaying data */
        /* Opens file in proper mode creates needed variables for displaying and comparing data, all creates the XPATH where the data I am looking for is stored */
        FILE * check_f_2;
        check_f_2 = fopen("player_2_info.txt", "r");
        char line_2[10000], nextPartLine_2[1000], final_line_2[1000];
        char* yards_p2 = (char *)malloc(sizeof(char) * 5);
        char* tds_p2 = (char *)malloc(sizeof(char) * 5);
        char* ints_p2 = (char *)malloc(sizeof(char) * 5);

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line_2, sizeof(line_2), check_f_2) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line_2, check) != NULL){
                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result_2_1 = strstr(line_2, check);
                int position_2_1 = result_2_1 - line_2 + strlen(check);
                printf ("Player 2 yards: ");
                for (int i = position_2_1, x = 0; i < position_2_1 + 4; i++, x++) {
                    printf("%c", line_2[i]);
                    yards_p2[x] = line_2[i];
                }
                /* All three data points I am looking for are on the same line in the HTML file, so I create a new line on which I look for the next and then the final data I need */
                for(int k = 0,  j = position_2_1 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    nextPartLine_2[k] = line_2[j];
                }


            /* Follows same process as above */
            if (strstr(nextPartLine_2, check) != NULL){
                char* result_2_2 = strstr(nextPartLine_2, check);
                int position_2_2 = result_2_2 - nextPartLine_2 + strlen(check);
                printf ("Player 2 touchdowns: ");
                for (int i = position_2_2, x = 0; i < position_2_2 + 2; i++, x++) {
                    if (isdigit(nextPartLine_2[i])){
                        printf("%c", nextPartLine_2[i]);
                        tds_p2[x] = nextPartLine_2[i];
                    }
                }
            for(int k = 0,  j = position_2_2 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    final_line_2[k] = nextPartLine_2[j];
                }
            }

            /* Follows same process as above */
            if (strstr(final_line_2, check) != NULL){
                char* result_2_3 = strstr(final_line_2, check);
                int position_2_3 = result_2_3 - final_line_2 + strlen(check);
                printf ("Player 2 interceptions: ");
                for (int i = position_2_3, x = 0; i < position_2_3 + 1; i++, x++) {
                    printf("%c \n", final_line_2[i]);
                    ints_p2[x] = final_line_2[i];
                }
            }
            }
        }


        int f_yds_p1 = (atoi(yards_p1));
        int f_tds_p1 = (atoi(tds_p1));
        int f_ints_p1 = (atoi(ints_p1));
        int f_yds_p2 = (atoi(yards_p2));
        int f_tds_p2 = (atoi(tds_p2));
        int f_ints_p2 = (atoi(ints_p2));
        int score_p1 = (f_yds_p1 * 0.4 + f_tds_p1 * 4 - f_ints_p1 * 2);
        int score_p2 = (f_yds_p2 * 0.4 + f_tds_p2 * 4 - f_ints_p2 * 2);
        if (score_p1 > score_p2){
            printf("\nThe fantasy assistant has determined Player 1 scored %d while Player 2 scored %d", score_p1, score_p2);
            printf("\nYou should start Player 1, as long as he's healthy and not on a bye \n\n");
        }
        if (score_p2 > score_p1){
            printf("\nThe fantasy assistant has determined Player 2 scored %d while Player 1 scored %d", score_p2, score_p1);
            printf("\nYou should start Player 2, as long as he's healthy and not on a bye \n\n");
        }






    return 0;

}




