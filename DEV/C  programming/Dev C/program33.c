//
// Created by User on 6/27/2023.
//Write a program to insert 10 elements and print them using array.

#include <stdio.h>

int main() {
    int a[10], i, j;
    int len = sizeof(a) / sizeof(int);

    for (i = 0; i < len; i++) {
        printf("Enter a number: ");
        scanf("%d", &a[i]);
    }

    for (j = 0; j < len; j++) {
        printf("%d ", a[j]);
    }


    return 0;
}
