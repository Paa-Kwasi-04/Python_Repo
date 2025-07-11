//
// Created by User on 8/3/2023.
//
#include "stdio.h"

int main(){
    int i=0,j=0,start,len;
    char main[60];
    char str[60];
    printf("Enter the main text: ");
    gets(main);
    printf("Enter start position string you want to delete: ");
    scanf("%d",&start);
    printf("Enter the len to delete: ");
    scanf("%d",&len);

    while(main[i] !='\0'){
        if(i == start){
            while(len>0){
                i++;
                len--;
            }
        }else{
        str[j] = main[i];
        j++;
        i++;
        }
    }

    str[i] = '\0';
    puts(str);







    return 0;
}