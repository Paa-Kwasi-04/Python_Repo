//
// Created by User on 8/1/2023.
//
#include "stdio.h"

int main(){
    int i = 0,j = 0,k = 0,p;
    char text[100];
    char str[30];
    char new_str[100];
    printf("Enter any text: ");
    gets(text);
    printf("Enter string to insert in text: ");
    gets(str);
    printf("Enter position to replace: ");
    scanf("%d",&p);

    while(text[i] != '\0'){  //loops through the text
        if(i == p){  // check if the looping process gets to the position where we want to input the string
            while (str[k] != '\0'){
                new_str[j] = str[k]; // the replaces the string at that given position
                j++;
                k++;
            }
        }else{   // else assign the character of the text at th given position to new_str
            new_str[j]  = text[i];
            j++;
        }
        i++;
    }
    new_str[j] = '\0';
    puts(new_str);



















    return 0 ;
}