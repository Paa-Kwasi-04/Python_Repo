//
// Created by User on 7/13/2023.
//
#include "stdio.h"

int main() {
    int num, bin = 0, rem, a[30];
    printf("Enter a number: ");
    scanf("%d", &num);

    for (int j = 0; num > 0; j++) {

        for (int i = 0; num > 0; i++) {
            rem = num % 2;
            num /= 2;
        }
    }

    printf("Binary :%d ", bin);


    return 0;
}
