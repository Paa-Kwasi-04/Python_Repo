//
// Created by User on 7/2/2023.
//Given a struct representing a student with fields: name (string), age (integer), and grade (float),
// write a C program to find the student with the highest grade in an array of students.

#include <stdio.h>
int i,j,k;

typedef struct student{
    char name[30];
    int age;
    float grade;
}Stu;

int main(){

    Stu st1 = {"kwasi",19,95};
    Stu st2 = {"kwame",18,100};
    Stu st3 = {"kwaku",20,80};
    Stu st4 = {"kofi",17,85};

    Stu myStu[4] = {st1,st2,st3,st4};
    int len = sizeof(myStu)/sizeof(Stu);

    // bubble sort to get the highest grade
    for(j = 0;j<len;j++){
        for(i = 0;i<len-1;i++){
            if(myStu[i].grade < myStu[i+1].grade){
                float c = myStu[i].grade;
                myStu[i].grade = myStu[i+1].grade;
                myStu[i+1].grade = c;
            }
        }
    }

    for(k = 0;k<len;k++){
        printf("%.2f ",myStu[k].grade);
    }
    printf("\n\nhighest  mark: %.2f",myStu[0].grade);
    return 0;
}