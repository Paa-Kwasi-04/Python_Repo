//
// Created by User on 6/20/2023.
//
//finding the sum of the first N odd numbers

#include <stdio.h>

int main() {
    int n;
    int sum = 0;
    // ask the user for the number of odd numbers
    printf("Enter the number of odd number: ");
    scanf("%d", &n);

    // finding the sum of first N odd numbers
    sum = n*n;

    printf("the sum is %d", sum);


    return 0;
}