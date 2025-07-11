//
// Created by User on 6/28/2023.
//Write a program to print Fibonacci sequence
// 0	1    1    2     3     5     8    13…… N terms and prints the sum of sequence.
#include <stdio.h>


int main() {
    int n, i, fibo ,a =-1,b = 1;

    printf("Enter the number of terms of the fibonacci: ");
    scanf("%d", &n);

    for (i = 0; i < n; i++) {
        fibo = a + b;
        a = b;
        b = fibo;

        printf("%d ",fibo);
    }
    return 0;
}















