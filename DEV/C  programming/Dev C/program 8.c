//
// Created by User on 6/15/2023.
//sum the first and last digit

#include <stdio.h>

int main(){
    int num,a,b,sum;
    //ask user for four-digit number
    printf("Enter a four digit number:");
    scanf("%d", &num);

    // getting the first digit we can use integer division by 1000 to get it
    a = num / 1000;

    // getting the last number we do a modulo 10
    b = num % 10;

    // getting the sum of the number
    sum = a + b;
    printf("the sum of the last and first digits is %d", sum);




    return 0;
}
//ask user for four-digit number
// sum the first and last digit