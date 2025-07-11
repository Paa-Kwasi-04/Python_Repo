e//
// Created by User on 6/15/2023.
//
#include <stdio.h>


int main() {
    int p, r, t;
    // asking for the principal
    printf("what is the principal amount\n");
    scanf("%d", &p);
    // asking for the rate
    printf("what is the rate \n");
    scanf("%d", &r);
    // asking for the time
    printf("For how many years ");
    scanf("%d", &t);

    int I = p * 0.01 * r * t;
    printf("the interest gained in a time of %d years is %d", t, I);


    return 0;
}
// calc for simple interest
// given P, R,t
