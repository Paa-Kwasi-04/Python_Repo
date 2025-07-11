//
// Created by User on 7/25/2023.
//deleting a string from a text
#include "stdio.h"


int main() {
    char text[60];
    char str2[60];
    char str3[60];
    int i = 0,j = 0,s,l,k = 0;
    printf("Enter a text : ");
    gets(text);
    printf("Enter position of substring to delete  : ");
    scanf("%d",&s);
    printf("Enter length of substring: ");
    scanf("%d",&l);


    while(text[i] != '\0'){
        if(i == s){
            while(l>0){
                l--;
                i++;
            }
        }else{
            str3[j] = text[i];
            j++;
        }
        i++;
    }

    str3[j] = '\0';
    puts(str3);

    return 0;
}