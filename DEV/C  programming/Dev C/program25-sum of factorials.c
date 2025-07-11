// Created by User on 6/21/2023.
// for getting the length of integers
// int len = floor(log10(abs(num)));
//Write a program to find the sum of following series:
//1! + 2! + 3! + 4! +... + n!

#include<stdio.h>

int main() {
    int num, i, j, fact = 1, x = 0;

    // ask the user for a number whose factorial is to be found
    printf("Enter any number: ");
    scanf("%d", &num);
    int Sum = 0;


    // finding the factorial of the number inputted

    for (j = 1; j <= num; j++) {
        Sum += fact;

        // does the factorial of each j value
        for (i = 0; x <= j; i++) {
            x++;
            fact *= x;
        }
    }

    // prints out the sum of the factorials
    printf("%d", Sum);


    return 0;
}

