//
// Created by User on 6/27/2023.
//Write a program to find minimum among 10 numbers using array.


#include <stdio.h>


int main() {
    int i, j, n, k;

    // create the array with user input
    printf("Enter the number elements in the array:");
    scanf("%d", &n);
    int a[n];
    for (i = 0; i < n; i++) {
        printf("Enter a number: ");
        scanf("%d", &a[i]);
    }


    // bubble sort the inputted array
    for (k = 0; k < n; k++) {
        for (j = 0; j < n ; j++) {
            //sorting in ascending order
            if (a[j] > a[j + 1]) {
                a[j] = a[j] + a[j + 1];
                a[j + 1] = a[j] - a[j + 1];
                a[j] = a[j] - a[j + 1];
            }
        }
    }
    //just to check the array after sorting
    for (k = 0; k < n; k++) {
        printf("%d ", a[k]);
    }
    // print out the smallest number in the array

    printf("\nThe smallest number: %d",a[0]);


    return 0;
}
