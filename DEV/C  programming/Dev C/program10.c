//
// Created by User on 6/20/2023.
//If the total selling price of 15 items and total profit earned on them is input through the keyboard,
// write a program to find the cost price of one item.

#include <stdio.h>

int main(){
    int tsp,tp;
    // ask user for total selling price for 15 items
    printf("Enter the total selling price:\n"); scanf("%d",&tsp);
    // ask user for the total profit
    printf("Enter the total profit:\n"); scanf("%d",&tp);

    int tcp = tsp - tp;
    float cp = (float) tcp / 15;

    printf("total cost price:%d\tcost price:%.2f",tcp,cp);





    return 0;
}