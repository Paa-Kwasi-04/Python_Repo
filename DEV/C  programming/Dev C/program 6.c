//
// Created by User on 6/15/2023.
//If a five-digit  number is input through the keyboard, write a program to calculate the sum of its digits.
// per observation this only calculates for 10 digits in a number


#include <stdio.h>

int main() {

    int num,sum = 0,i,rem;
    // ask user for a five digit number
    printf("Enter any number: ");
    scanf("%d", &num);
    int no = num;

    // get the sum of the numbers in the digits
    i = 0;
    while ( num !=0) {
        rem = num % 10;
        num /= 10;
        sum += rem;
        i++;
    }

    printf("%d is the sum of the digits of %d", sum,no);


    return 0;
}
