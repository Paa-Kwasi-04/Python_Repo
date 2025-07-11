//
// Created by User on 7/1/2023.
//Write a C program that uses a struct to represent a student's information(name, roll number, and marks in three subjects).
//The program should take input for three students and display their details along with the average marks.
#include <stdio.h>

// create global struct
typedef struct student{
    char name[20];
    int roll_no;
    int Physics;
    int Maths;
    int Chemistry;
    int average;
}student;

// take input from students
// then display the information together with the average of their scores

int main(){
    int i,j,k,roll,phy,maths,chem,ave;
    char name[20];


    for(k = 0; k< 3;k++){

        for(j = 0;j< 3;j++){
            student std = {.name = name,.roll_no = roll,.average = ave};

            for(i = 0;i < 1;i++){
                printf("Enter your name: "); fgets(name,sizeof(name) , stdin);
                printf("Enter your roll number: "); scanf("%d",&roll);
                printf("Enter Physics mark: "); scanf("%d", &phy);
                printf("Enter Maths mark: "); scanf("%d", &maths);
                printf("Enter Chemistry mark: "); scanf("%d", &chem);

                ave = (phy+maths+chem)/2;
             }
        }
    }

    return 0;
}