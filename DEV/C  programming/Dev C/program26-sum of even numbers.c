//
// Created by User on 6/22/2023.
//Write a program to find the sum of following series:
//S = 2+4+6+8+……………N terms.

#include <stdio.h>


int main(){
    int N, sum = 0;

    //ask the user for the N even numbers to add
    printf("Enter number of even number series you are adding:");
    scanf("%d", &N);

    // finding the sum of the even numbers in question
    // use a series and sequence
    // for even numbers U = a +(n-1)d at n = 2,d = 2
    sum = N*N + N;

    printf("%d",sum);
    return 0;
}
