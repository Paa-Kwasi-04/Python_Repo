//
// Created by User on 8/1/2023.
//
#include <stdio.h>
#include "string.h"

int main() {
    // Initial work on strings in W3
    // Creating a function to append a string to another; you can use the string function strcat()

    char dest_string[50], source_string[50];
    printf("Enter the destination string: ");
    gets(dest_string);
    printf("Enter the source string: ");
    gets(source_string);
    int i,j=0;
    int len = strlen(dest_string);
    i = len;
    while (source_string[j] != '\0'){
        dest_string[i] = source_string[j];
        i++;
        j++;
    }
    dest_string[i] = '\0';
    printf("The new destination string is %s",dest_string);

    // Another way to append two strings
    /*for (int i=0;i<total_len;i++){
        if (i<len1){
            str3[i] = str1[i];
        }else{
            str3[i] = str2[i-len1];
        }
    }
    printf("The concatenated string is %s",str3);
     */


    return 0;
}
