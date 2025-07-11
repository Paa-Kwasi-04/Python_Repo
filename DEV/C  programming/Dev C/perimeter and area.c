//
// Created by User on 1/23/2024.
// write a program to compute the perimeter and area of a circle with a given radius
#include "stdio.h"
#define pi 3.412


int main(){
    float r;
    printf("Enter radius of a circle: ");
    scanf("%f",&r);

    float area = pi * r * r;
    float peri = 2 * pi * r;

    printf("Area: %f\t Perimeter: %f",area,peri);






    return 0;
}
