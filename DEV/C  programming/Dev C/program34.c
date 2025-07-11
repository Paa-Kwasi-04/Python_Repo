//
// Created by User on 6/27/2023.
//Write a program in C to accept an integer numbers and find sum of digits.

#include <stdio.h>

int main() {
    int  n, i, sum = 0,j;

    // sets the length of the array
    printf("How many numbers do you want to enter: ");
    scanf("%d", &n);
    int a[n];

    // inputs values into the array
    for (i = 0; i < n; i++) {
        printf("Enter the %d number:",i+1);
        scanf("%d", &a[i]);
    }
    // sums the numbers in the array
    for(j = 0;j<n;j++){
        sum += a[j];
    }

    printf("sum : %d",sum);

    return 0;
}
