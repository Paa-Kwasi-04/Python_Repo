//
// Created by User on 9/13/2023.
//having problems
#include "stdio.h"
#include "string.h"

void strings(char x[],int a){
    int i,y[a];

    for(i = 0;x[i] != '\0';i++){
        if(x[i]>= 'a' && x[i]<= 'c'){
            y[i] = x[i] -32;
        }else{
            y[i] = x[i];
            continue;
        }
    }
    y[i] = '\0';
    printf("%s",y);
}

int main(){
    char name[20];

    printf("Enter your name: ");
    gets(name);
    int len = strlen(name);

    strings(name,len);
}