//
// Created by User on 6/20/2023.
//Write a menu-driven program to perform addition, subtraction, multiplication & division operations.

#include <stdio.h>
#include <conio.h>

int main(){
    int choice,a,b;
    // creating the Menu

    printf("---MENU---\n");
    printf("1.Addition\n");
    printf("2.Subtraction\n");
    printf("3.Multiplication\n");
    printf("4.Division\n");

    printf("Choose from the Menu above:\n");
    scanf("%d",&choice);

    // getting the two numbers from the user

    printf("Enter any number: "); scanf("%d",&a);
    printf("Enter another number: "); scanf("%d",&b);

    switch (choice) {
        default:
            printf("Please choose from the menu ") ;
        case 1:
            printf("The Sum is %d",(a+b));
            break;
        case 2:
            printf("The difference is &d",(a-b));
            break;
        case 3:
            printf("The product is %d",(a*b));
            break;
        case 4:
            if(b!=0){
                printf("The quotient is %d",(a/b));
                break;
            }else{
                printf("This division is not possible");
                break;
            }
    }

    return 0;
}
