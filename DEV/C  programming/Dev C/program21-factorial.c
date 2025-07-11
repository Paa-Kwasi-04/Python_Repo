//
// Created by User on 6/20/2023.
//Write a program to find the factorial of any number using for loop.


#include <stdio.h>


int main() {
    int num, i, fact = 1, x = 1;

    // ask the user for a number whose factorial is to be found
    printf("Enter any number: ");
    scanf("%d", &num);

    // finding the factorial of the number inputted
    for (i = 0; x <= num; i++) {
        fact *= x;
        x++;
    }

    printf("%d", fact);


    return 0;
}
