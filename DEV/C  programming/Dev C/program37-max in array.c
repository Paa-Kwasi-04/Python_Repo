//
// Created by User on 6/27/2023.
//WAP to find greatest among 10 numbers using array.


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
        //always let it be j<n-1 for bubble sorting
        for (j = 0; j < n-1 ; j++) {
            //this sorts in descending ord
            if (a[j] < a[j + 1]) {
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
    // print out the biggest number in the array

    printf("\nThe biggest number: %d",a[0]);


    return 0;
}

