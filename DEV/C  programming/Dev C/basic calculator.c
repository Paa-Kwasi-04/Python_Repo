//
// Created by User on 8/27/2023.
//
#include "stdio.h"

int calc(int x, int y,char z){
    switch (z) {
        case '+':
            return x+y;
        case '-':
            return x-y;
        case 'x':
            return x * y;
        case '/':
            return x / y;
        default:
            return 0;
    }
}



int main(){
    int a,b;
    char op;
    printf("Enter a number: ");
    scanf("%d",&a);
    printf("Enter another number: ");
    scanf("%d",&b);
    printf("Enter operation: ");
    gets(op);


    int result = calc(a,b,op);
    printf("%d",result)









    return 0;
}