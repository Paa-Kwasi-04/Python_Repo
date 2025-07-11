//
// Created by User on 1/23/2024.
//  write a program that accepts two integers from the user and adds, pdts them
#include "stdio.h"


int main() {
    int a, b;
    printf("Enter first number: ");
    scanf("%d", &a);
    printf("Enter second number: ");
    scanf("%d", &b);


    printf("Sum: %d\nProduct: %d", (a + b), (a * b));


    return 0;
}
