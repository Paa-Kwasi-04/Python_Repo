//
// Created by User on 6/6/2023.
//
#include <stdio.h>

int main() {
    // get two integers from the user
    int a, b;
    printf("Enter a value for a: ");
    scanf("%d", &a);
    printf("Enter a value for b: ");
    scanf("%d", &b);

    // swap the values of the numbers
    a = a + b;
    b = a - b;
    a = a - b;
    // Display the variables with their values been swapped
    printf("%d and %d are the values for a and b respectfully", a, b);


    return 0;
}