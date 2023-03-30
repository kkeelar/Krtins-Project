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


/* Writes HTML File into a text file for the first URL for parsing, call this function back into the main function */
static size_t write_data(void *ptr, size_t size, size_t nmemb, void *stream){
  size_t written = fwrite(ptr, size, nmemb, (FILE *)stream);
  return written;
}



/* Writes HTML File into a text file for the seconed URL parsing, call this function back into the main function */
static size_t write_data_1(void *ptr, size_t size, size_t nmemb, void *stream){
  size_t written = fwrite(ptr, size, nmemb, (FILE *)stream);
  return written;
}


// Main method, takes the number of arguments
int main(int agrc, char *argv[]) {


    /* Determines which if statement to use, depenedent on the posistion the user wants to compare */
    string input = argv[1];
    string check_input_1 = "QB";
    string check_input_2 = "WR";
    string check_input_3 = "RB";

    /* Tells the user if they forgot to put a proper input */
    if(agrc!=2){
        printf("Opps, you forgot to pick a posistion\n");
        return 1;
    }



    if (input [0] == check_input_1[0] && input[1] == check_input_1[1]){
        /* Prints help menu for the user */
        printf ("\nWelcome to fantasy QB assistant \n");
        printf ("\nWe know picking a week to week starter is hard, so we're gonna help you out \n");
        printf ("\nJust enter the two Qb's you want to compare like this (patrick-mahomes-ii)  \n");

        /* Developing the first URL for player 1*/
        char url[] = "https://www.foxsports.com/nfl/";
        string P1 = get_string("\nEnter QB1: ");
        char player_1[strlen(P1)];
        for (int y = 0; y < strlen(P1); y++){
            player_1[y] = P1[y];
        }
        player_1[strlen(P1)] = '\0';
        char add_on[] = "-player";
        strcat(url, player_1);
        strcat(url, add_on);

        /* Developing the seconed URL for player 2*/
        char url_2[] = "https://www.foxsports.com/nfl/";
        string P2 = get_string("\nEnter QB2: ");
        char player_2[strlen(P2)];
        for (int z = 0; z < strlen(P2); z++){
            player_2[z] = P2[z];
        }
        player_2[strlen(P2)] = '\0';
        char add_on_1[] = "-player";
        strcat(url_2, player_2);
        strcat(url_2, add_on_1);

        /* Prints new line */
        printf("\n");

        /* Intilizaes the libray, finds the proper URL to pull from, and writes the data into a file with a call back function */
        CURL *curl = curl_easy_init();
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);


        /* Writes the data into the proper file */
        FILE * f_1;
        f_1 = fopen("player_1_info.txt", "wb");
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, f_1);

        /* Retrieves the proper data, if issue in pulling data, tells user */
        CURLcode result_1 = curl_easy_perform(curl);
        if (result_1 != CURLE_OK){
            printf("Uh oh, check if input is proper");
        }

        /* Proper clean up */
        fclose(f_1);
        curl_easy_cleanup(curl);

        /* Process of gathering and displaying data */

        /* Opens file in proper mode creates needed variables for displaying and comparing data, all creates the XPATH where the data I am looking for is stored */
        FILE * check_f_1;
        check_f_1 = fopen("player_1_info.txt", "r");
        string check = "<span class=\"fs-23 cl-wht\">";
        char line[10000];
        //int yards_p1 = 0;
        int tds_p1 = 0;
        int ints_p1 = 0;
        char* yards_p1 = (char *)malloc(sizeof(char) * 5);

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line, sizeof(line), check_f_1) != NULL) {

            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line, check) != NULL){

                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result = strstr(line, check);
                int position = result - line + strlen(check);
                printf ("%s yards: ", P1);
                for (int i = position, x = 0, y = 1000; i < position + 4; i++, x++) {
                    //if (isdigit(line[i])){
                    printf("%c", line[i]);
                    yards_p1[i] = line[i];
                    //strcat(yards_p1, &line[i]);
                    printf("this is yards **************************  %c \n", yards_p1[i]);
                    //printf("this is y %d, this is line[%d]: %c \n", y, i, line[i]);
                    //printf("This is yards: %d \n", yards_p1);
                    //printf ("this is calc %c * %d = %d \n", line[i], y, (line[i] * y));
                    //yards_p1 = yards_p1 + line[i] * y;
                    //printf("this is yards %d \n", yards_p1);
                    y = y / 10;
                }

                printf("Step 1 \n");
                for (int x = 0; x <= 3; x++){
                    printf ("This is yards %c \n", yards_p1[x]);
                }
                printf("Step 2 \n");



                /* All three data points I am looking for are on the same line in the HTML file, so I create a new line on which I look for the next and then the final data I need */
                char nextPartLine[1000];
                for(int k = 0,  j = position + strlen(check); j < sizeof(line) ; j++, k++) {
                    nextPartLine[k] = line[j];
                }

            /* Follows same process as above */
            char final_line[1000];
            if (strstr(nextPartLine, check) != NULL){
                char* result_1 = strstr(nextPartLine, check);
                int position_1 = result_1 - nextPartLine + strlen(check);
                printf ("\n%s touchdowns: ", P1);
                for (int i = position_1, x = 0, y = 1000; i < position_1 + 2; i++, x++) {
                    if (isdigit(nextPartLine[i])){
                        printf("%c", nextPartLine[i]);
                        tds_p1 = tds_p1 + nextPartLine[i] * y;
                        y = y / 10;
                    }
                }

                for(int k = 0,  j = position_1 + strlen(check); j < sizeof(line) ; j++, k++) {
                    final_line[k] = nextPartLine[j];
                }
            }

            /* Follows same process for the final data location */
            if (strstr(final_line, check) != NULL){
                char* result_2 = strstr(final_line, check);
                int position_2 = result_2 - final_line + strlen(check);
                printf ("\n%s interceptions: ", P1);
                for (int i = position_2, x = 0; i < position_2 + 1; i++, x++) {
                    if (isdigit(final_line[i])){
                        printf("%c \n", final_line[i]);
                        ints_p1 = final_line[i];
                    }
                }
            }
        }
    }


        //printf("this is yards %d, this is tds %d, this is ints %d", yards_p1, tds_p1, ints_p1);




        printf ("\n");


        /* Follows exact same process as above but for player 2 with a new URL and I need to use a seperate call back function */
        CURL *curl_1 = curl_easy_init();
        curl_easy_setopt(curl_1, CURLOPT_URL, url_2);
        curl_easy_setopt(curl_1, CURLOPT_WRITEFUNCTION, write_data_1);

        FILE * f_2;
        f_2 = fopen("player_2_info.txt", "wb");

        curl_easy_setopt(curl_1, CURLOPT_WRITEDATA, f_2);
        CURLcode result_2 = curl_easy_perform(curl_1);
        if (result_2 != CURLE_OK){
            printf("Uh oh, check if input is proper");
        }
        fclose(f_2);
        curl_easy_cleanup(curl_1);

        FILE * check_f_2;
        check_f_2 = fopen("player_2_info.txt", "r");
        char line_2[10000];
        //char yards_p2[3];
        //char tds_p2[2];
        //char ints_p2[1];
        while(fgets(line_2, sizeof(line_2), check_f_2) != NULL) {
            //string check = "<span class=\"fs-23 cl-wht\">";

            if (strstr(line_2, check) != NULL){
                char* result_2_1 = strstr(line_2, check);
                int position_2_1 = result_2_1 - line_2 + strlen(check);
                printf ("%s yards: ", P2);
                for (int i = position_2_1, x = 0; i < position_2_1 + 4; i++, x++) {
                    if (isdigit(line_2[i])){
                        printf("%c", line_2[i]);
                        //yards_p2[x] = line_2[i];
                        //printf("this is player 1 yards: %c , this is player 2 yards: %c \n", yards_p1[x], yards_p2[x]);
                        //printf("this is yards_p1[%d]: %c \n", x, yards_p1[x]);
                    }
                }
                char nextPartLine_2[1000];
                for(int k = 0,  j = position_2_1 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    nextPartLine_2[k] = line_2[j];
                }
            char final_line_2[1000];
            if (strstr(nextPartLine_2, check) != NULL){
                char* result_2_2 = strstr(nextPartLine_2, check);
                int position_2_2 = result_2_2 - nextPartLine_2 + strlen(check);
                printf ("\n%s touchdowns: ", P2);
                for (int i = position_2_2, x = 0; i < position_2_2 + 2; i++, x++) {
                    if (isdigit(nextPartLine_2[i])){
                        printf("%c", nextPartLine_2[i]);
                        //tds_p2[x] = nextPartLine_2[i];
                    }
                }

                for(int k = 0,  j = position_2_2 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    final_line_2[k] = nextPartLine_2[j];
                }
            }
            if (strstr(final_line_2, check) != NULL){
                char* result_2_3 = strstr(final_line_2, check);
                int position_2_3 = result_2_3 - final_line_2 + strlen(check);
                printf ("\n%s interceptions: ", P2);
                for (int i = position_2_3, x = 0; i < position_2_3 + 1; i++, x++) {
                    if (isdigit(final_line_2[i])){
                        printf("%c \n", final_line_2[i]);
                        //ints_p2[x] = final_line_2[i];
                    }
                }
            }
            }

        }


    }

/*
    if (input [0] == check_input_2[0] && input[1] == check_input_2[1]){

        /* Same process as the first function, but for a different posistion, follows all the same functions and methods */

        printf ("\nWelcome to fantasy WR assistant \n");
        printf ("\nWe know picking a week to week starter is hard, so we're gonna help you out \n");
        printf ("\nJust enter the two WR's you want to compare like this (julio-jones)  \n");

        char url[] = "https://www.foxsports.com/nfl/";
        string P1 = get_string("\nEnter WR1: ");
        char player_1[strlen(P1)];
        for (int y = 0; y < strlen(P1); y++){
            player_1[y] = P1[y];
        }
        player_1[strlen(P1)] = '\0';
        char add_on[] = "-player";
        strcat(url, player_1);
        strcat(url, add_on);

        char url_2[] = "https://www.foxsports.com/nfl/";
        string P2 = get_string("\nEnter WR2: ");
        char player_2[strlen(P2)];
        for (int z = 0; z < strlen(P2); z++){
            player_2[z] = P2[z];
        }
        player_2[strlen(P2)] = '\0';
        char add_on_1[] = "-player";
        strcat(url_2, player_2);
        strcat(url_2, add_on_1);

        printf("\n");


        CURL *curl = curl_easy_init();
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);

        FILE * f_1;
        f_1 = fopen("player_1_info.txt", "wb");
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, f_1);
        CURLcode result_1 = curl_easy_perform(curl);

        if (result_1 != CURLE_OK){
            printf("Uh oh, check if input is proper");
        }

        fclose(f_1);
        curl_easy_cleanup(curl);

        FILE * check_f_1;
        check_f_1 = fopen("player_1_info.txt", "r");

        string check = "<span class=\"fs-23 cl-wht\">";
        char line[10000];
        char yards_p1[3];
        char tds_p1[2];
        char ints_p1[1];


        while(fgets(line, sizeof(line), check_f_1) != NULL) {
            if (strstr(line, check) != NULL){
                char* result = strstr(line, check);
                int position = result - line + strlen(check);
                printf ("%s yards: ", P1);
                for (int i = position, x = 0; i < position + 4; i++, x++) {
                    if (isdigit(line[i])){
                        printf("%c", line[i]);
                        yards_p1[x] = line[i];
                        //printf("this is yards_p1[%d]: %c \n", x, yards_p1[x]);
                    }
                }
                char nextPartLine[1000];
                for(int k = 0,  j = position + strlen(check); j < sizeof(line) ; j++, k++) {
                    nextPartLine[k] = line[j];
                }

            char final_line[1000];
            if (strstr(nextPartLine, check) != NULL){
                char* result_1 = strstr(nextPartLine, check);
                int position_1 = result_1 - nextPartLine + strlen(check);
                printf ("\n%s receptions: ", P1);
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

            if (strstr(final_line, check) != NULL){
                char* result_2 = strstr(final_line, check);
                int position_2 = result_2 - final_line + strlen(check);
                printf ("\n%s touchdowns: ", P1);
                for (int i = position_2, x = 0; i < position_2 + 1; i++, x++) {
                    if (isdigit(final_line[i])){
                        printf("%c \n", final_line[i]);
                        ints_p1[x] = final_line[i];
                    }
                }
            }
            }

        }



        printf ("\n");

        /* Follows the same process as the functions above */
        CURL *curl_1 = curl_easy_init();
        curl_easy_setopt(curl_1, CURLOPT_URL, url_2);
        curl_easy_setopt(curl_1, CURLOPT_WRITEFUNCTION, write_data_1);
        FILE * f_2;
        f_2 = fopen("player_2_info.txt", "wb");
        curl_easy_setopt(curl_1, CURLOPT_WRITEDATA, f_2);
        CURLcode result_2 = curl_easy_perform(curl_1);
        if (result_2 != CURLE_OK){
            printf("Uh oh, check if input is proper");
        }
        fclose(f_2);
        curl_easy_cleanup(curl_1);
        FILE * check_f_2;
        check_f_2 = fopen("player_2_info.txt", "r");

        char line_2[10000];
        char yards_p2[3];
        char tds_p2[2];
        char ints_p2[1];

        while(fgets(line_2, sizeof(line_2), check_f_2) != NULL) {
            if (strstr(line_2, check) != NULL){
                char* result_2_1 = strstr(line_2, check);
                int position_2_1 = result_2_1 - line_2 + strlen(check);
                printf ("%s yards: ", P2);
                for (int i = position_2_1, x = 0; i < position_2_1 + 4; i++, x++) {
                    if (isdigit(line_2[i])){
                        printf("%c", line_2[i]);
                        yards_p2[x] = line_2[i];
                    }
                }
                char nextPartLine_2[1000];
                for(int k = 0,  j = position_2_1 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    nextPartLine_2[k] = line_2[j];
                }
            char final_line_2[1000];
            if (strstr(nextPartLine_2, check) != NULL){
                char* result_2_2 = strstr(nextPartLine_2, check);
                int position_2_2 = result_2_2 - nextPartLine_2 + strlen(check);
                printf ("\n%s receptions: ", P2);
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
            if (strstr(final_line_2, check) != NULL){
                char* result_2_3 = strstr(final_line_2, check);
                int position_2_3 = result_2_3 - final_line_2 + strlen(check);
                printf ("\n%s touchdowns: ", P2);
                for (int i = position_2_3, x = 0; i < position_2_3 + 1; i++, x++) {
                    if (isdigit(final_line_2[i])){
                        printf("%c \n", final_line_2[i]);
                        ints_p2[x] = final_line_2[i];
                    }
                }
            }
            }

        }
        return 0;

    }


    if (input[0] == check_input_3[0] && input[1] == check_input_3[1]){

        /* Follows same process as the above functions, different URLS and different players */

        printf ("\nWelcome to fantasy RB assistant \n");
        printf ("\nWe know picking a week to week starter is hard, so we're gonna help you out \n");
        printf ("\nJust enter the two RB's you want to compare like this (dalvin-cook)  \n");

        char url[] = "https://www.foxsports.com/nfl/";
        string P1 = get_string("\nEnter RB1: ");
        char player_1[strlen(P1)];
        for (int y = 0; y < strlen(P1); y++){
            player_1[y] = P1[y];
        }
        player_1[strlen(P1)] = '\0';
        char add_on[] = "-player";
        strcat(url, player_1);
        strcat(url, add_on);

        char url_2[] = "https://www.foxsports.com/nfl/";
        string P2 = get_string("\nEnter RB2: ");
        char player_2[strlen(P2)];
        for (int z = 0; z < strlen(P2); z++){
            player_2[z] = P2[z];
        }
        player_2[strlen(P2)] = '\0';
        char add_on_1[] = "-player";
        strcat(url_2, player_2);
        strcat(url_2, add_on_1);

        printf("\n");

        CURL *curl = curl_easy_init();
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_data);

        FILE * f_1;
        f_1 = fopen("player_1_info.txt", "wb");

        curl_easy_setopt(curl, CURLOPT_WRITEDATA, f_1);
        CURLcode result_1 = curl_easy_perform(curl);

        if (result_1 != CURLE_OK){
            printf("Uh oh, check if input is proper");
        }

        fclose(f_1);
        curl_easy_cleanup(curl);

        FILE * check_f_1;
        check_f_1 = fopen("player_1_info.txt", "r");

        string check = "<span class=\"fs-23 cl-wht\">";
        char line[10000];
        char yards_p1[3];
        char tds_p1[2];
        char ints_p1[1];


        while(fgets(line, sizeof(line), check_f_1) != NULL) {
            if (strstr(line, check) != NULL){
                char* result = strstr(line, check);
                int position = result - line + strlen(check);
                printf ("%s yards: ", P1);
                for (int i = position, x = 0; i < position + 4; i++, x++) {
                    if (isdigit(line[i])){
                        printf("%c", line[i]);
                        yards_p1[x] = line[i];
                        //printf("this is yards_p1[%d]: %c \n", x, yards_p1[x]);
                    }
                }
                char nextPartLine[1000];
                for(int k = 0,  j = position + strlen(check); j < sizeof(line) ; j++, k++) {
                    nextPartLine[k] = line[j];
                }
            char final_line[1000];
            if (strstr(nextPartLine, check) != NULL){
                char* result_1 = strstr(nextPartLine, check);
                int position_1 = result_1 - nextPartLine + strlen(check);
                printf ("\n%s attempts: ", P1);
                for (int i = position_1, x = 0; i < position_1 + 3; i++, x++) {
                    if (isdigit(nextPartLine[i])){
                        printf("%c", nextPartLine[i]);
                        tds_p1[x] = nextPartLine[i];
                    }
                }

                for(int k = 0,  j = position_1 + strlen(check); j < sizeof(line) ; j++, k++) {
                    final_line[k] = nextPartLine[j];
                }
            }
            if (strstr(final_line, check) != NULL){
                char* result_2 = strstr(final_line, check);
                int position_2 = result_2 - final_line + strlen(check);
                printf ("\n%s touchdowns: ", P1);
                for (int i = position_2, x = 0; i < position_2 + 1; i++, x++) {
                    if (isdigit(final_line[i])){
                        printf("%c \n", final_line[i]);
                        ints_p1[x] = final_line[i];
                    }
                }
            }
            }

        }



        printf ("\n");

        /* Follows same process as above, different players and URL's */

        CURL *curl_1 = curl_easy_init();
        curl_easy_setopt(curl_1, CURLOPT_URL, url_2);
        curl_easy_setopt(curl_1, CURLOPT_WRITEFUNCTION, write_data_1);

        FILE * f_2;
        f_2 = fopen("player_2_info.txt", "wb");

        curl_easy_setopt(curl_1, CURLOPT_WRITEDATA, f_2);
        CURLcode result_2 = curl_easy_perform(curl_1);

        if (result_2 != CURLE_OK){
            printf("Uh oh, check if input is proper");
        }

        fclose(f_2);
        curl_easy_cleanup(curl_1);

        FILE * check_f_2;
        check_f_2 = fopen("player_2_info.txt", "r");

        char line_2[10000];
        char yards_p2[3];
        char tds_p2[2];
        char ints_p2[1];

        while(fgets(line_2, sizeof(line_2), check_f_2) != NULL) {
            if (strstr(line_2, check) != NULL){
                char* result_2_1 = strstr(line_2, check);
                int position_2_1 = result_2_1 - line_2 + strlen(check);
                printf ("%s yards: ", P2);
                for (int i = position_2_1, x = 0; i < position_2_1 + 4; i++, x++) {
                    if (isdigit(line_2[i])){
                        printf("%c", line_2[i]);
                        yards_p2[x] = line_2[i];
                        //printf("this is player 1 yards: %c , this is player 2 yards: %c \n", yards_p1[x], yards_p2[x]);
                        //printf("this is yards_p1[%d]: %c \n", x, yards_p1[x]);
                    }
                }
                char nextPartLine_2[1000];
                for(int k = 0,  j = position_2_1 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    nextPartLine_2[k] = line_2[j];
                }
            char final_line_2[1000];
            if (strstr(nextPartLine_2, check) != NULL){
                char* result_2_2 = strstr(nextPartLine_2, check);
                int position_2_2 = result_2_2 - nextPartLine_2 + strlen(check);
                printf ("\n%s attempts: ", P2);
                for (int i = position_2_2, x = 0; i < position_2_2 + 3; i++, x++) {
                    if (isdigit(nextPartLine_2[i])){
                        printf("%c", nextPartLine_2[i]);
                        tds_p2[x] = nextPartLine_2[i];
                    }
                }

                for(int k = 0,  j = position_2_2 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    final_line_2[k] = nextPartLine_2[j];
                }
            }
            if (strstr(final_line_2, check) != NULL){
                char* result_2_3 = strstr(final_line_2, check);
                int position_2_3 = result_2_3 - final_line_2 + strlen(check);
                printf ("\n%s touchdowns: ", P2);
                for (int i = position_2_3, x = 0; i < position_2_3 + 1; i++, x++) {
                    if (isdigit(final_line_2[i])){
                        printf("%c \n", final_line_2[i]);
                        ints_p2[x] = final_line_2[i];
                    }
                }
            }
            }

        }
        return 0;

    }




    /* Returns zero to terminate the function */
    return 0;


}













