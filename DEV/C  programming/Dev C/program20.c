//
// Created by User on 6/20/2023.
//Admission to a professional course is subject to the following condition math>=60, phy>=50, chem>= 40.
// Write a program for finding that candidates are eligible or not

#include <stdio.h>

int main(){
    int i = 1,math,phy,chem;

    while(i == 1){
        printf("Enter maths score:"); scanf("%d",&math);
        printf("Enter physics score:"); scanf("%d",&phy);
        printf("Enter chemistry score:"); scanf("%d",&chem);

        if(math>=  60 && phy >= 50 && chem >= 40){
            printf("You are eligible for this course");
        }
        else{
            printf("You don't qualify for admission");
            break;
        }
        printf("\nWould you like to continue: ");
        scanf("%d",&i);

    }

    printf("\nYou have ended the program :)");

    return 0;
}