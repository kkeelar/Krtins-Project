
#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include <ctype.h>
#include <curl/curl.h>

/* Function to build first URL, takes player name 1 created in the "who_is_better" function to build the first URL and passes it through the function */
char * build_url1(string player) {

    /* builds empty array to store information into */
    static char url1[100];

    /* Intalizes the empty array and copies a blank into it, then copies the beggining of every URL into it */
    strcpy(url1, "");
    strcpy(url1, "https://www.foxsports.com/nfl/");

    /* Builds the name of the player provided into a usable variable for the URL builder */
    char player_1[strlen(player)];
    for (int y = 0; y < strlen(player); y++){
        player_1[y] = player[y];
    }

    /* Eliminates any extra charecters that may have been added, then adds the player name and final portion of the URL before returning the finished URL */
    player_1[strlen(player)] = '\0';
    char add_on[] = "-player";
    strcat(url1, player_1);
    strcat(url1, add_on);
    return url1;
}

/* Function to build the seconed array, follows exact same process as above function */
char * build_url2(string player) {
    static char url2[100];
    strcpy(url2, "");
    strcpy(url2, "https://www.foxsports.com/nfl/");
    char player_2[strlen(player)];
    for (int y = 0; y < strlen(player); y++){
        player_2[y] = player[y];
    }
    player_2[strlen(player)] = '\0';
    char add_on[] = "-player";
    strcat(url2, player_2);
    strcat(url2, add_on);
    return url2;
}

/* Procedure to gather the information on both player's stats this year and calculates which player to start, calls the URL building functions */
void who_is_better(string position) {

        /* Prints help menu for the user */
        printf ("\n Welcome to Kel Miper, the 2023-2024 Fantasy Draft Expert \n");
        printf ("\n We're here to help with the stress of draft day, the biggest day of the year ! \n");
        printf ("\n Just enter the two %ss you're thinking of drafting like so (firstname-lastname)  \n\n", position);

        /* Gathers input for building the URL's */
        string player1 = get_string(" Player 1: ");
        string player2 = get_string("\n Player 2: ");

        /* Calls proper function to build the URL's, passes through the players name as a paramter to build the correct URL. */
        /* Builds two seperate variables for two seperate URL's for two seperate players */
        char url_player1[100];
        strcpy(url_player1, build_url1(player1));
        char url_player2[100];
        strcpy(url_player2, build_url2(player2));

        /* Prints new line */
        printf("\n");

        /* Intilizaes the libray, finds the proper URL to pull from */
        CURL *curl = curl_easy_init();
        curl_easy_setopt(curl, CURLOPT_URL, url_player1);

        /* Writes the data into the proper file */
        FILE * f_1;
        f_1 = fopen("player_1_info.txt", "wb");
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, f_1);

        /* Retrieves the proper data, if issue in pulling data */
        curl_easy_perform(curl);
        /* Proper clean up */
        fclose(f_1);
        curl_easy_cleanup(curl);

        /* Process of gathering and displaying data */
        /* Opens file in proper mode creates needed variables for displaying and comparing data, creates the XPATH where the data I am looking for is stored */
        FILE * check_f_1;
        check_f_1 = fopen("player_1_info.txt", "r");
        string check = "<span class=\"fs-23 cl-wht\">";
        char line[10000];
        char nextPartLine[1000];
        char final_line [1000];
        int check_if_worked_1 = 0;
        char* yards_p1 = (char *)malloc(sizeof(char) * 5);
        char* stat1_p1 = (char *)malloc(sizeof(char) * 5);
        char* stat2_p1 = (char *)malloc(sizeof(char) * 5);

        /* Variables to change output depenedent on the input provided */
        /* For example, running backs can't throw interceptions but FOX spors stores interceptions in the same XPATH as rushing attempts */
        string stat_1, stat_2;
        if (strchr(position, 'Q') != NULL){
            stat_1 = "tocuhdowns";
            stat_2 = "interceptions";
        }
        if (strchr(position, 'W') != NULL){
            stat_1 = "receptions";
            stat_2 = "touchdowns";
        }
        if (strchr(position, 'R') != NULL && (strchr(position, 'B') != NULL)){
            stat_1 = "attempts";
            stat_2 = "touchdowns";
        }

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line, sizeof(line), check_f_1) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this for loop */
            if (strstr(line, check) != NULL){
                check_if_worked_1 += 1;
                /* Finds location of the XPATH I am looking for in the text file and prints the proper data where it is located */
                char* result = strstr(line, check);
                int position = result - line + strlen(check);
                printf (" %s yards: ", player1);
                /* Finds where the data I am looking for is and prints it as long as it's actually a digit */
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
            /* Follows same process as above, cuts the rest of the data I am looking for into a for loop and stores it into a new array for me to scan through */
            if (strstr(nextPartLine, check) != NULL){
                char* result_1 = strstr(nextPartLine, check);
                int position_1 = result_1 - nextPartLine + strlen(check);
                printf ("\n %s %s: ", player1, stat_1);
                /* Finds where the data I am looking for is and prints it as long as it's actually a digit */
                for (int i = position_1, x = 0; i < position_1 + 3; i++, x++) {
                    if (isdigit(nextPartLine[i])){
                        printf("%c", nextPartLine[i]);
                        stat1_p1[x] = nextPartLine[i];
                    }
                }
            /* All three data points I am looking for are on the same line in the HTML file, so I create a new line on which I look for the next and then the final data I need */
            for(int k = 0,  j = position_1 + strlen(check); j < sizeof(line) ; j++, k++) {
                    final_line[k] = nextPartLine[j];
                }
            }
            /* Follows same process as above, takes the rest of the data left on the line and looks through it with the check variable */
            if (strstr(final_line, check) != NULL){
                char* result_2 = strstr(final_line, check);
                int position_2 = result_2 - final_line + strlen(check);
                printf ("\n %s %s: ", player1, stat_2);
                /* Finds where the data I am looking for is and prints it as long as it's actually a digit */
                for (int i = position_2, x = 0; i < position_2 + 2; i++, x++) {
                    if (isdigit(final_line[i])){
                        printf("%c", final_line[i]);
                        stat2_p1[x] = final_line[i];
                    }
                }
            }
            }
        }


        /* Here I check if the URL was properly built and if CURL was able to grab the URL */
        if (check_if_worked_1 == 0){
            printf (" Uh oh, looks like the first player you entered is an unusable player \n");
            printf (" Make sure all your inputs are correct and in the proper format \n");
        }

        /* Prints new line */
        printf("\n");
        printf("\n");

        /* Intilizaes the libray, finds the proper URL to pull from */
        CURL *curl_1 = curl_easy_init();
        curl_easy_setopt(curl_1, CURLOPT_URL, url_player2);
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
        char line_2[10000];
        char nextPartLine_2[1000];
        char final_line_2[1000];
        int check_if_worked_2 = 0;
        char* yards_p2 = (char *)malloc(sizeof(char) * 5);
        char* stat1_p2 = (char *)malloc(sizeof(char) * 5);
        char* stat2_p2 = (char *)malloc(sizeof(char) * 5);

        /* Reads through each line of the file with the raw HTML info */
        while(fgets(line_2, sizeof(line_2), check_f_2) != NULL) {
            /* If the XPATH with the data I am looking for is found, follow this info */
            if (strstr(line_2, check) != NULL){
                check_if_worked_2 += 1;
                /* Finds location of the XPATH I am looking for and prints the proper data where it is located */
                char* result_2_1 = strstr(line_2, check);
                int position_2_1 = result_2_1 - line_2 + strlen(check);
                printf (" %s yards: ", player2);
                /* Finds where the data I am looking for is and prints it as long as it's actually a digit */
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
            /* Follows same process as above, cuts the rest of the data I am looking for into a for loop */
            if (strstr(nextPartLine_2, check) != NULL){
                char* result_2_2 = strstr(nextPartLine_2, check);
                int position_2_2 = result_2_2 - nextPartLine_2 + strlen(check);
                printf ("\n %s %s: ", player2, stat_1);
                /* Finds where the data I am looking for is and prints it as long as it's actually a digit */
                for (int i = position_2_2, x = 0; i < position_2_2 + 3; i++, x++) {
                    if (isdigit(nextPartLine_2[i])){
                        printf("%c", nextPartLine_2[i]);
                        stat1_p2[x] = nextPartLine_2[i];
                    }
                }
            /* All three data points I am looking for are on the same line in the HTML file, so I create a new line on which I look for the next and then the final data I need */
            for(int k = 0,  j = position_2_2 + strlen(check); j < sizeof(line_2) ; j++, k++) {
                    final_line_2[k] = nextPartLine_2[j];
                }
            }
            /* Follows same process as above, takes the rest of the data left on the line and looks through it with the check variable */
            if (strstr(final_line_2, check) != NULL){
                char* result_2_3 = strstr(final_line_2, check);
                int position_2_3 = result_2_3 - final_line_2 + strlen(check);
                printf ("\n %s %s: ", player2, stat_2);
                /* Finds where the data I am looking for is and prints it as long as it's actually a digit */
                for (int i = position_2_3, x = 0; i < position_2_3 + 2; i++, x++) {
                    if (isdigit(final_line_2[i])){
                        printf("%c", final_line_2[i]);
                        stat2_p2[x] = final_line_2[i];
                    }
                }
            }
            }
        }

        /* Here I check if the URL was properly built and if CURL was able to grab the URL */
        if (check_if_worked_2 == 0){
            printf(" Uh oh, looks like the seconed player you entered is an unsuable player\n");
            printf(" Make sure all your inputs are correct and in the proper format \n");
        }

        /* Prints new line */
        printf("\n");
        printf("\n");

        /* Comparison between the scores of the players, different posistions have different calculations for score */
        /* Variables are made as integers in order compare the stats between the two players */
        int f_yds_p1 = (atoi(yards_p1));
        int f_stat1_p1 = (atoi(stat1_p1));
        int f_stat2_p1 = (atoi(stat2_p1));
        int f_yds_p2 = (atoi(yards_p2));
        int f_stat1_p2 = (atoi(stat1_p2));
        int f_stat2_p2 = (atoi(stat2_p2));
        int score_p1;
        int score_p2;

        /* Calculation for the QB score */
        if (strchr(position, 'Q') != NULL){
            score_p1 = (f_yds_p1 * 0.4 + f_stat1_p1 * 4 - f_stat1_p1 * 2);
            score_p2 = (f_yds_p2 * 0.4 + f_stat2_p2 * 4 - f_stat2_p2 * 2);
        }
        /* Calculation for the WR score */
        else if (strchr(position, 'W') != NULL){
            score_p1 = (f_yds_p1 * 1 + f_stat1_p1 * 1 + f_stat2_p1 * 6);
            score_p2 = (f_yds_p2 * 1 + f_stat1_p2 * 1 + f_stat2_p2 * 6);
        }
        /* Calculation for the RB score */
        else{
            score_p1 = (f_yds_p1 * 1 + f_stat1_p1 * 0.5 - f_stat2_p1 * 2);
            score_p2 = (f_yds_p2 * 1 + f_stat1_p2 * 0.5 - f_stat2_p2 * 2);
        }

        /* Final output based on the score the two players receieved */
        if (score_p1 > score_p2){
            printf(" The fantasy assistant has determined %s scored %d while %s scored %d \n", player1, score_p1, player2, score_p2);
            printf("\n You should start %s, as long as he's healthy and not on a bye \n\n", player1);
        }
        if (score_p2 > score_p1){
            printf(" The fantasy assistant has determined %s scored %d while %s scored %d", player2, score_p2, player1, score_p1);
            printf("\n You should draft %s, as long as he's healthy \n\n", player2);
        }
        // End of function
}


/* Main method, main entry point and calls upon above functions and procedures */
int main(int agrc, char *argv[]) {

    /* Tells user if they didn't provide enough command line arguments */
    if(agrc!=2){
        printf("Oops, you forgot to pick a posistion\n\n");
        printf("Usage : ./fantasy_football_assistant QB | WR | RB \n\n");
        return 1;
    }

    /* Takes user input */
    string input = argv[1];

    /* Tells user if they didn't provide the correct command line argument */
    if (strchr(input, 'Q') == NULL && strchr(input, 'B') == NULL && strchr(input, 'R') == NULL && strchr(input, 'W') == NULL){
        printf ("Oops, you did not pick a proper posisiton, check your spelling and that it's capital \n");
        printf("Usage : ./fantasy__football_assistant QB | WR | RB \n");
        return 1;
    }

    /* Calls the who_is_better procedure with the posistion as input and exits the function */
    who_is_better(input);
    exit(0);
}













