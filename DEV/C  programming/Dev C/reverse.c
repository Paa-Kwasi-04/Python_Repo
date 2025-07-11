//
// Created by User on 1/23/2024.
// write a program to print the xtic xml in the reverse order

#include "stdio.h"
#include "string.h"


int main(){
    char word[20];
    printf("Enter a word: ");
    scanf("%s",word);

    printf("Word reversed: %s",strrev(word));



    return 0;
}