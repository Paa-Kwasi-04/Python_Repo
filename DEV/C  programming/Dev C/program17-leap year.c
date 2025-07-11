//
// Created by User on 6/28/2023.
//Any year is input through the keyboard. Write a program to determine whether the year is a leap year or not.
//A year is a leap year if it is divisible by 4.
//However, if the year is divisible by 100, it is not a leap year, unless...
//The year is also divisible by 400, in which case it is a leap year.
// so if the last two digits of the number is divisible by 4 then it a multiple of four
#include <stdio.h>
int year,lastDigit ;

void leap_year(int *y){

    lastDigit = *y % 100;
    if(lastDigit % 4 == 0 ||(*y % 400 ==0 && *y % 100 != 0)){
        printf("\n%d is leap",year);
    }else{
        printf("\n%d is not leap",year);
    }

}

int main() {
    printf("Enter a year: ");
    scanf("%d",&year);
    leap_year(&year);

    return 0;
}
