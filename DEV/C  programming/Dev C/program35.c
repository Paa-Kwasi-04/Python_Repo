//
// Created by User on 6/27/2023.
//Write a program to multiply 10 numbers using array.

#include <stdio.h>

int main() {
    int  n, i, pro = 1,j;

    // sets the length of the array
    printf("How many numbers do you want to enter: ");
    scanf("%d", &n);
    int a[n];

    // inputs values into the array
    for (i = 0; i < n; i++) {
        printf("Enter the %d number:",i+1);
        scanf("%d", &a[i]);
    }
    // multiplies the numbers in the array
    for(j = 0;j<n;j++){
        pro *= a[j];
    }

    printf("product : %d",pro);

    return 0;
}
