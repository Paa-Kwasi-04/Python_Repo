//
// Created by User on 7/25/2023.
//
#include "stdio.h"

int main(){
    char s1[100],i =0,j = 0;
    char s2[100];

    printf("Enter for s1: ");
    gets(s1);
    printf("Enter for s2: ");
    gets(s2);

    // this gets the length of s1
    while(s1[i] != '\0'){
        i++;
    }
    //So in the second while loop the i starts at the length of s1
    while(s2[j] !='\0'){
        s1[i] = s2[j];
        i++;
        j++;
    }

    puts(s1);











    return 0;
}
