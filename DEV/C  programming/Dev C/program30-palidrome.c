//
// Created by User on 6/27/2023.
//WAP to find the reverse of a number and check whether it is palindrome or not.
#include <stdio.h>

int main() {
    int i, num, rem, rev = 0;
    printf("Enter a number: ");
    scanf("%d", &num);
    int rep = num;

    for (i = 0; num > 0; i++) {
        rem = num % 10;
        rev = rev * 10 + rem;
        num /= 10;
    }

    if (rep == rev) {
        printf("The number is a palindrome");
    } else {
        printf("The number is not a palindrome");
    }


    return 0;
}

