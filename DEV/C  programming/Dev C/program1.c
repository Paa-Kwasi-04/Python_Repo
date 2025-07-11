//// TODO: I will have to comeback to this
// Created by User on 6/21/2023.
// Basic salary is input through the keyboard. His dearness allowance is 40% of basic salary,
// and house rent allowance is 20% of basic salary. Write a program to calculate his gross salary.
#include <stdio.h>

int main() {
    int salary;
    // use a for loop to ask users salary
    printf("Enter your basic: ");
    scanf("%d", &salary);

    float dearness = 0.4 * salary;
    float houseRent = 0.2 * salary;

    float gross_salary = salary - (dearness+houseRent);






    return 0;
}
