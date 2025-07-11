//
// Created by User on 7/25/2023.
// A-Z in ascii is 65-91 and a-z in ascii code is 97-123
//the difference btn the upper and lower case of alphanumeric characters is 32
#include "stdio.h"

int main() {
    char str[100], i = 0;
    char upper[100];
    char lower[100];
    printf("Enter a string\n");
    gets(str);

    //gets the upper case
    while (str[i] != '\0') {
        if ('a' <= str[i] && str[i] <= 'z') {
            upper[i] = str[i] - 32;
        } else {
            upper[i] = str[i];
        }
        i++;
    }

    // gets the lower case
    for(int k = 0; str[k] != '\0';k++){
        if ('A' <= str[k] && str[k] <= 'Z') {
            lower[k] = str[k] + 32;
        } else {
            lower[k] = str[k];
        }
    }
    puts(lower);
    puts(upper);    // it is the same as printf   operation but used for strings

    return 0;

}