//
// Created by User on 6/15/2023.
//
// find  the greatest number amongst three numbers using nested if loops

#include <stdio.h>


int main() {
    int a, b, c;
    // ask the user for three numbers
    printf("Enter first number:");
    scanf("%d", &a);
    printf("Enter second number:");
    scanf("%d", &b);
    printf("Enter third number:");
    scanf("%d", &c);

//     use nested if loops to get the greatest number
    if (a > b) {
        if (a > c) {
            printf("%d is the greatest", a);
        } else  {
            printf("%d is the greatest", c);
        }
    }else  {
        if (b>c) {
            printf("%d is the greatest", b);
        } else  {
            printf("%d is the greatest", c);
        }
    }



    return 0;
}