//
// Created by User on 6/20/2023.
//Write a program to calculate greatest among two numbers.

#include <stdio.h>

int main() {
    int a, b;
    //ask the user for two numbers
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("Enter another number: ");
    scanf("%d", &b);

    int r = (a > b) ? 1 : 0;

    if (r) {
        printf("the greatest number: %d", a);
    } else {
        printf("the greatest number: %d", b);
    }


    return 0;
}
