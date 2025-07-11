//
// Created by User on 6/21/2023.
//Write a program to find the factorial of any number using do while.
#include <stdio.h>


int main(){
    int num,i ,fact = 1,no = 1;

    // ask the user for a number whose factorial is to be found
    printf("Enter any number: "); scanf("%d",&num);

    // finding the factorial of the number inputted
    i = 0;
    do {
        fact *= no;
        no++;
        i++;
    }while(i < num );

    printf("%d",fact);


    return 0;
}