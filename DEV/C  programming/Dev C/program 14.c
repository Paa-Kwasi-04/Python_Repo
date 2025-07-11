//
// Created by User on 6/20/2023.
// Write a program to calculate greatest among three numbers using multiple if statement.

#include <stdio.h>

int main(){
    int a,b,c;
// ask the user for the three numbers
    printf("Enter number_1: ");scanf("%d",&a);
    printf("Enter number_2: ");scanf("%d",&b);
    printf("Enter number_3: ");scanf("%d",&c);

    if(a>b && a> c){
        printf("the greatest number is %d",a);
    }
    if(b>a && b>c){
        printf("the greatest number is %d",b);
    }
    if(c>a && c>b){
        printf("the greatest number is %d",c);
    }

    return 0;
}
