#include "ctype.h"
#include "stdio.h"
#include "stdlib.h"
#include "string.h"


const char* digit_words[10] = {
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
};

void get_firstlast(char* line, int* first, int* last) {
    uint64_t len = strlen(line);
    int first_set = 0;
    size_t i = 0;
    size_t first_idx = 0;
    size_t last_idx = 0;
    while (i < len) {
        // one digit char
        if (isdigit(line[i])) {
            *last = line[i] - '0';
            last_idx = i;
            if (!first_set) {
                *first = line[i] - '0';
                first_idx = i;
                first_set = 1;
            }
            i++;
            continue;
        }

        i++;
    }

    for (size_t digit_idx = 0; digit_idx < 10; digit_idx++) {
        char* s = NULL;
        if (s = strstr(line, digit_words[digit_idx])) {
            size_t word_idx = s - line;
            if (word_idx <= first_idx) {
                *first = digit_idx;
                first_idx = word_idx;
            }

            // find last occurence of this word
            size_t check_idx = word_idx + strlen(digit_words[digit_idx]);
            for (;;) {
                if (check_idx >= strlen(line))
                    break;
                char* next_word = NULL;
                if (!(next_word = strstr(line + check_idx, digit_words[digit_idx]))) {
                    break;
                }
                
                word_idx = next_word - line;
                check_idx = word_idx + strlen(digit_words[digit_idx]);
            }

            if (word_idx >= last_idx) {
                *last = digit_idx;
                last_idx = word_idx;

            }
        }
    }
    
    return;
}
 

int main(int argc, char* argv[]) {
    uint64_t total = 0;
    
    FILE * fp;
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    fp = fopen("input.txt", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);
    
    while ((read = getline(&line, &len, fp)) != -1) {
        int first, last;
        get_firstlast(line, &first, &last);
        
        total += (first * 10) + last;
    }
    fclose(fp);
    if (line)
        free(line);
    
    printf("Total: %u\n", total);


    return 0;
}