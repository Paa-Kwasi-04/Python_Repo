//
// Created by User on 7/6/2023.
//
#include <stdio.h>

int main() {
    int i, j, n, num = 0;
    printf("Enter number of elements in the array: ");
    scanf("%d", &n);
    int a[n];

    for (i = 0; i < n; i++) {
        printf("Enter any number: ");
        scanf("%d", &a[i]);
    }

    // forms the numbers from the array
    for (j = 0; j < n; j++) {
       num =num*10 + a[j] ;
    }
    printf("the number generated is: %d", num);

    return 0;
}
