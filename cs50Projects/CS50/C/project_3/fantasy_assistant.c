#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <ctype.h>
#include <curl/curl.h>


/* Writes HTML File into a text file for the first URL for parsing, call this function back into the main function */
static size_t p1_URL(void *ptr, size_t size, size_t nmemb, void *stream){
  size_t written = fwrite(ptr, size, nmemb, (FILE *)stream);
  return written;
}

/* Writes HTML File into a text file for the seconed URL parsing, call this function back into the main function */
static size_t p2_URL(void *ptr, size_t size, size_t nmemb, void *stream){
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
        printf("Oops, you forgot to pick a posistion\n");
        return 1;
    }

    if (input [0] == check_input_1[0] && input[1] == check_input_1[1]){
        /* Prints help menu for the user */
        printf ("\nWelcome to fantas \n");
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
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, p1_URL);
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
        char nextPartLine[1000];
        char final_line [1000];
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
                printf ("%s yards: ", P1);
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
                printf ("\n%s touchdowns: ", P1);
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
                printf ("\n%s interceptions: ", P1);
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
        curl_easy_setopt(curl_1, CURLOPT_URL, url_2);
        curl_easy_setopt(curl_1, CURLOPT_WRITEFUNCTION, p2_URL);

        /* Writes data into the proper file */
        FILE * f_2;
        f_2 = fopen("player_2_info.txt", "wb");
        curl_easy_setopt(curl_1, CURLOPT_WRITEDATA, f_2);
        CURLcode result_2 = curl_easy_perform(curl_1);
        if (result_2 != CURLE_OK){
            printf("Uh oh, check if input is proper");
        }
        /* Clean up */
        fclose(f_2);
        curl_easy_cleanup(curl_1);

        /* Process of gathering and displaying data */
        /* Opens file in proper mode creates needed variables for displaying and comparing data, all creates the XPATH where the data I am looking for is stored */
        FILE * check_f_2;
        check_f_2 = fopen("player_2_info.txt", "r");
        char line_2[10000];
        char nextPartLine_2[1000];
        char final_line_2[1000];
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
                printf ("%s yards: ", P2);
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
                printf ("\n%s touchdowns: ", P2);
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
                printf ("\n%s interceptions: ", P2);
                for (int i = position_2_3, x = 0; i < position_2_3 + 1; i++, x++) {
                    printf("%c \n", final_line_2[i]);
                    ints_p2[x] = final_line_2[i];

                }
            }

            }
        }


        /* Final Calculations for each score */
        int f_yds_p1 = (atoi(yards_p1));
        int f_tds_p1 = (atoi(tds_p1));
        int f_ints_p1 = (atoi(ints_p1));
        int f_yds_p2 = (atoi(yards_p2));
        int f_tds_p2 = (atoi(tds_p2));
        int f_ints_p2 = (atoi(ints_p2));
        int score_p1 = (f_yds_p1 * 0.4 + f_tds_p1 * 4 - f_ints_p1 * 2);
        int score_p2 = (f_yds_p2 * 0.4 + f_tds_p2 * 4 - f_ints_p2 * 2);

        /* Final print out for each player */
        if (score_p1 > score_p2){
            printf("\nThe fantasy assistant has determined %s scored %d while %s scored %d", P1, score_p1, P2, score_p2);
            printf("\nYou should start %s, as long as he's healthy and not on a bye \n\n", P1);
        }
        if (score_p2 > score_p1){
            printf("\nThe fantasy assistant has determined %s scored %d while %s scored %d", P2, score_p2, P1, score_p1);
            printf("\nYou should start %s, as long as he's healthy and not on a bye \n\n", P2);
        }
        return 0;
    }

    /* Wide Reciever Assistant */

    if (input [0] == check_input_2[0] && input[1] == check_input_2[1]){

        /* Prints help menu for the user */
        printf ("\nWelcome  assistant \n");
        printf ("\nWe know picking a week to week starter is hard, so we're gonna help you out \n");
        printf ("\nJust enter the two WR's you want to compare like this (julio-jones)  \n");

        /* Developing the first URL for player 1*/
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

        /* Developing the seconed URL for player 2*/
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

        /* Prints new line */
        printf("\n");

        /* Intilizaes the libray, finds the proper URL to pull from, and writes the data into a file with a call back function */
        CURL *curl = curl_easy_init();
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, p1_URL);

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
        char nextPartLine[1000];
        char final_line [1000];
        char* yards_p1 = (char *)malloc(sizeof(char) * 5);
        char* rec_p1 = (char *)malloc(sizeof(char) * 5);
        char* tds_p1 = (char *)malloc(sizeof(char) * 5);

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line, sizeof(line), check_f_1) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line, check) != NULL){
                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result = strstr(line, check);
                int position = result - line + strlen(check);
                printf ("%s Yards: ", P1);
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
                printf ("\n%s Receptions: ", P1);
                for (int i = position_1, x = 0; i < position_1 + 2; i++, x++) {
                    if (isdigit(nextPartLine[i])){
                        printf("%c", nextPartLine[i]);
                        rec_p1[x] = nextPartLine[i];
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
                printf ("\n%s Touchdowns: ", P1);
                for (int i = position_2, x = 0; i < position_2 + 1; i++, x++) {
                    if (isdigit(final_line[i])){
                        printf("%c \n", final_line[i]);
                        tds_p1[x] = final_line[i];
                    }
                }
            }

            }
        }

        printf ("\n");

        /* Follows exact same process as above but for player 2 with a new URL and I need to use a seperate call back function */
        CURL *curl_1 = curl_easy_init();
        curl_easy_setopt(curl_1, CURLOPT_URL, url_2);
        curl_easy_setopt(curl_1, CURLOPT_WRITEFUNCTION, p2_URL);

        FILE * f_2;
        f_2 = fopen("player_2_info.txt", "wb");

        curl_easy_setopt(curl_1, CURLOPT_WRITEDATA, f_2);
        CURLcode result_2 = curl_easy_perform(curl_1);
        if (result_2 != CURLE_OK){
            fprintf(stderr, "curl_easy_perform() failed: %s\n", curl_easy_strerror(result_2));
        }
        fclose(f_2);
        curl_easy_cleanup(curl_1);

        FILE * check_f_2;
        check_f_2 = fopen("player_2_info.txt", "r");
        char line_2[10000];
        char nextPartLine_2[1000];
        char final_line_2[1000];
        char* yards_p2 = (char *)malloc(sizeof(char) * 5);
        char* rec_p2 = (char *)malloc(sizeof(char) * 5);
        char* tds_p2 = (char *)malloc(sizeof(char) * 5);

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line_2, sizeof(line_2), check_f_2) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line_2, check) != NULL){
                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result_2_1 = strstr(line_2, check);
                int position_2_1 = result_2_1 - line_2 + strlen(check);
                printf ("%s Yards: ", P2);
                for (int i = position_2_1, x = 0; i < position_2_1 + 4; i++, x++) {
                    if (isdigit(line_2[i])){
                        printf("%c", line_2[i]);
                        yards_p2[x] = line_2[i];
                    }
                }
                /* All three data points I am looking for are on the same line in the HTML file, so I create a new line on which I look for the next and then the final data I need */
                for(int k = 0,  j = position_2_1 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    nextPartLine_2[k] = line_2[j];
                }


            /* Follows same process as above */
            if (strstr(nextPartLine_2, check) != NULL){
                char* result_2_2 = strstr(nextPartLine_2, check);
                int position_2_2 = result_2_2 - nextPartLine_2 + strlen(check);
                printf ("\n%s Receptions: ", P2);
                for (int i = position_2_2, x = 0; i < position_2_2 + 2; i++, x++) {
                    if (isdigit(nextPartLine_2[i])){
                        printf("%c", nextPartLine_2[i]);
                        rec_p2[x] = nextPartLine_2[i];
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
                printf ("\n%s Touchdowns: ", P2);
                for (int i = position_2_3, x = 0; i < position_2_3 + 1; i++, x++) {
                    if (isdigit(final_line_2[i])){
                        printf("%c \n", final_line_2[i]);
                        tds_p2[x] = final_line_2[i];
                    }
                }
            }

            }
        }


        /* Final Calculations for each score */
        int f_yds_p1 = (atoi(yards_p1));
        int f_rec_p1 = (atoi(rec_p1));
        int f_tds_p1 = (atoi(tds_p1));

        int f_yds_p2 = (atoi(yards_p2));
        int f_rec_p2 = (atoi(rec_p2));
        int f_tds_p2 = (atoi(tds_p2));

        int score_p1 = (f_yds_p1 * 1 + f_rec_p1 * 1 + f_tds_p1 * 6);
        int score_p2 = (f_yds_p2 * 1 + f_rec_p2 * 1 + f_tds_p2 * 6);

        /* Final print out for each player */
        if (score_p1 > score_p2){
            printf("\nThe fantasy assistant has determined %s scored %d while %s scored %d", P1, score_p1, P2, score_p2);
            printf("\n You should start %s, as long as he's healthy and not on a bye \n\n", P1);
        }
        if (score_p2 > score_p1){
            printf("\nThe fantasy assistant has determined %s scored %d while %s scored %d", P2, score_p2, P1, score_p1);
            printf("\nYou should start %s, as long as he's healthy and not on a bye \n\n", P2);
        }
    }

    /* Running Back assistant */

    if (input [0] == check_input_3[0] && input[1] == check_input_3[1]){

        /* Prints help menu for the user */
        printf ("\nWelcome to fantasy Running backs fantasy assistant \n");
        printf ("\nWe know picking a week to week starter is hard, so we're gonna help you out \n");
        printf ("\nJust enter the two RB's you want to compare like this (dalvin-cook) keep it lower case and a dash between name \n");

        /* Developing the first URL for player 1*/
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

        /* Developing the seconed URL for player 2*/
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

        /* Prints new line */
        printf("\n");

        /* Intilizaes the libray, finds the proper URL to pull from, and writes the data into a file with a call back function */
        CURL *curl = curl_easy_init();
        curl_easy_setopt(curl, CURLOPT_URL, url);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, p1_URL);


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
        char nextPartLine[1000];
        char final_line [1000];
        char* yards_p1 = (char *)malloc(sizeof(char) * 5);
        char* atps_p1 = (char *)malloc(sizeof(char) * 5);
        char* tds_p1 = (char *)malloc(sizeof(char) * 5);

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line, sizeof(line), check_f_1) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line, check) != NULL){
                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result = strstr(line, check);
                int position = result - line + strlen(check);
                printf ("%s Yards: ", P1);
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
                printf ("\n%s Attempts: ", P1);
                for (int i = position_1, x = 0; i < position_1 + 2; i++, x++) {
                    if (isdigit(nextPartLine[i])){
                        printf("%c", nextPartLine[i]);
                        atps_p1[x] = nextPartLine[i];
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
                printf ("\n%s Touchdowns: ", P1);
                for (int i = position_2, x = 0; i < position_2 + 1; i++, x++) {
                    if (isdigit(final_line[i])){
                        printf("%c \n", final_line[i]);
                        tds_p1[x] = final_line[i];
                    }
                }
            }

            }
        }

        printf ("\n");

        /* Follows exact same process as above but for player 2 with a new URL and I need to use a seperate call back function */
        CURL *curl_1 = curl_easy_init();
        curl_easy_setopt(curl_1, CURLOPT_URL, url_2);
        curl_easy_setopt(curl_1, CURLOPT_WRITEFUNCTION, p2_URL);

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
        char nextPartLine_2[1000];
        char final_line_2[1000];
        char* yards_p2 = (char *)malloc(sizeof(char) * 5);
        char* atps_p2 = (char *)malloc(sizeof(char) * 5);
        char* tds_p2 = (char *)malloc(sizeof(char) * 5);

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line_2, sizeof(line_2), check_f_2) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line_2, check) != NULL){
                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result_2_1 = strstr(line_2, check);
                int position_2_1 = result_2_1 - line_2 + strlen(check);
                printf ("%s Yards: ", P2);
                for (int i = position_2_1, x = 0; i < position_2_1 + 4; i++, x++) {
                    if (isdigit(line_2[i])){
                        printf("%c", line_2[i]);
                        yards_p2[x] = line_2[i];
                    }
                }
                /* All three data points I am looking for are on the same line in the HTML file, so I create a new line on which I look for the next and then the final data I need */
                for(int k = 0,  j = position_2_1 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    nextPartLine_2[k] = line_2[j];
                }


            /* Follows same process as above */
            if (strstr(nextPartLine_2, check) != NULL){
                char* result_2_2 = strstr(nextPartLine_2, check);
                int position_2_2 = result_2_2 - nextPartLine_2 + strlen(check);
                printf ("\n%s Attempts: ", P2);
                for (int i = position_2_2, x = 0; i < position_2_2 + 2; i++, x++) {
                    if (isdigit(nextPartLine_2[i])){
                        printf("%c", nextPartLine_2[i]);
                        atps_p2[x] = nextPartLine_2[i];
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
                printf ("\n%s Touchdowns: ", P2);
                for (int i = position_2_3, x = 0; i < position_2_3 + 1; i++, x++) {
                    if (isdigit(final_line_2[i])){
                        printf("%c \n", final_line_2[i]);
                        tds_p2[x] = final_line_2[i];
                    }
                }
            }

            }
        }

        /* Final Calculations for each score */
        int f_yds_p1 = (atoi(yards_p1));
        int f_atps_p1 = (atoi(atps_p1));
        int f_tds_p1 = (atoi(tds_p1));

        int f_yds_p2 = (atoi(yards_p2));
        int f_atps_p2 = (atoi(atps_p2));
        int f_tds_p2 = (atoi(tds_p2));

        int score_p1 = (f_yds_p1 * 1 + f_atps_p1 * 0.5 + f_tds_p1 * 6);
        int score_p2 = (f_yds_p2 * 1 + f_atps_p2 * 0.5 + f_tds_p2 * 6);


        /* Final print out for each player */
        if (score_p1 > score_p2){
            printf("\n %s scored %d while %s scored %d", P1, score_p1, P2, score_p2);
            printf("\nYou should start %s, as long as he's healthy and not on a bye \n\n", P1);
        }
        if (score_p2 > score_p1){
            printf("\nThe fantasy assistant has determined %s scored %d while %s scored %d", P2, score_p2, P1, score_p1);
            printf("\nYou should start %s, as long as he's healthy and not on a bye \n\n", P2);
        }
    }


    /* Returns zero to terminate the function */
    return 0;


}













