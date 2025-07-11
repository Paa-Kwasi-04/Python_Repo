// Created by User on 1/23/2024.
//
//write a  program to print your name , date of birth and mobile number


#include "stdio.h"



int main(){
    char name[30],date[10];
    int num;

    printf("Enter your name: ");
    scanf("%s",name);
    printf("\nEnter date of birth(dd/mm/yy): ");
    scanf("%s", date);
    printf("\nEnter Telephone: ");
    scanf("%d", &num);
    printf("\n");
    printf("Name: %s\tDate of Birth: %s\tNumber: %d",name,date,num);

    return 0;
}