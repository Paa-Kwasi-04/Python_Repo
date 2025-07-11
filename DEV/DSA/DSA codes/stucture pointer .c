//
// Created by User on 9/13/2023.
//
#include "stdio.h"

typedef struct student{
    int roll_num;
    int marks;
}s;

s stu[1]; int i;

int main(){
    //creating the whole array of structures
    for(i = 0;i< sizeof(stu);i++){
        printf("Enter roll number of stu[%d]: ",i);
        scanf("%d",&stu[i].roll_num);
        printf("\nEnter the marks of stu[%d]: ",i);
        scanf("%d",&stu[i].marks);
    }

    //printing out the array of structures created
    for(i = 0;i<sizeof(stu);i++){
        printf( "%d      %d ",stu[i].roll_num,stu[i].marks);
    }





    return 0;
}