//
// Created by User on 6/20/2023.
//A library charges a fine for every book returned late.
// For first 5 days the fine is 50 paisa, for 6-10 days, fine is one rupee and above 10 days, fine is 5 rupees.
// If you return the book after 30 days your membership will be cancelled.
// Write a program to accept the number of days the member is late to return the book and display the fine or appropriate message.
////TODO : I have to come back and complete the code
#include <stdio.h>

int main(){

    int numberOfDays;
    printf("How many days has the member kept the after due date:\n"); scanf("%d",&numberOfDays);

    if(0< numberOfDays <= 5){
        printf("You must pay a fine of 50 pesa");
    }
    else if(5<numberOfDays <= 10){
        printf("You must pay a fine of one rupee");
    }





    return 0;
}