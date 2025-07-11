//
// Created by User on 6/20/2023.
//The length and breadth of a rectangle and radius of a circle are input through the keyboard.
// Write a program to calculate the area & perimeter of the rectangle, and the area & circumference of the circle.


#include <stdio.h>

int main() {
    int len, wid, r;
    // ask user for length, width and radius
    printf("Enter length of rectangle:");
    scanf("%d", &len);
    printf("\nEnter width of rectangle: ");
    scanf("%d", &wid);
    printf("\nEnter radius of circle: ");
    scanf("%d", &r);

    // calculate the perimeter
    int peri = 2 * (len + wid);
    int area = len * wid;
    int cir = 2 * 3.14 * r;
    int area_circle = 3.14 * r * r;

    printf("rectangular area:%d\trectangular perimeter:%d\n",area,peri);
    printf("circular area:%d\tcircumference:%d\n",area_circle,cir);


    return 0;
}