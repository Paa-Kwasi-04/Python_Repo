//
// Created by User on 6/20/2023.
//syntax for loop
// for(initial variable value,condition to check)
#include <stdio.h>

int main() {
    int i;
    int sum = 0;

    int marks[5];

    for (i = 0; i < 5; i++) {
        printf("enter marks:");
        scanf("%d", &marks[i]);
    }
    for (i = 0; i < 5; i++) {
        sum += marks[i];
    }

    float percent = (float) sum / 5;

    printf("Aggregate: %d\t percentage:%f", sum, percent);


    return 0;
}