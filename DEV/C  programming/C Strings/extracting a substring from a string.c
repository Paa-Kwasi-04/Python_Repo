//
// Created by User on 8/1/2023.
//
#include "stdio.h"


int main(){
    int i , f,j = 0,l;
    char substr[20];
    char str[30];
    printf("Enter the main string: ");
    gets(str);
    printf("Enter the position of the first character of substring: ");
    scanf("%d",&f) ;
    printf("Enter the length of the substring: ");
    scanf("%d",&l);
    i = f;

    while(str[f] != '\0' && l>0){
        substr[j] = str[i];
        f++;
        j++;
        l--;
    }
    substr[j] = '\0';    // we put this here to end the created string with a null
    puts(substr);













    return 0;
}