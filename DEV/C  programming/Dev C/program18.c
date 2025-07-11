//
// Created by User on 6/20/2023.
//A five-digit number is entered through the keyboard.
// Write a program to obtain the reverse number and
// to determine whether the original and reversed number are equal or not.

#include <stdio.h>
#include <math.h>

int main(){

    int num, i, rem, rev = 0;

    // ask  user for number
    printf("Enter a four digit number:");
    scanf("%d", &num);
    int no = num;


    // reversing the number
    for (i = 0;num > 0; ++i) {
       rem = num %10;
       rev = rev*10 + rem;
       num /= 10;
    }

    printf("%d\n",rev );
// checking if the original and the reversed numbers are equal
    if(no == rev){
        printf("the original and the reverse are equal");
    }else{
        printf("the original and the reverse are not equal");
    }

    return 0;
}