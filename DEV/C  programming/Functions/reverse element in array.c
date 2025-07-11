//
// Created by User on 7/2/2023.
//Implement a C program to reverse the elements of an integer array in place.


#include <stdio.h>

int main() {
    int i;
    int a[5] = {1, 2, 3, 4, 5};
    int len = sizeof(a) / sizeof(int);

    for (i = len - 1; i >= 0; i--) {
        printf("%d ", a[i]);
    }


    return 0;
}
