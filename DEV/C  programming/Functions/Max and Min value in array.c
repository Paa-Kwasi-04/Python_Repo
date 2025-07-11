//
// Created by User on 6/29/2023.
//Given an integer array, write a C program to find the maximum and minimum elements in the array.


#include <stdio.h>

int main() {
    int marks[4];
    int n = sizeof(marks) / sizeof(int);

    // getting user to create the array for the marks
    for (int j = 0; j < n; j++) {
        printf("Enter marks of student: ");
        scanf("%d", &marks[j]);
    }
    int min = 0;
    int temp = marks[min];
    int i = 0, k = 0;
    while (i < n){
        if(marks[min] > marks[k])
            min = k;
            k++;
        i++;
    }

    if(marks[min] != temp){
        printf("Least Value: %d",marks[min]);
    }else{
        printf("Least Value: %d",temp);
    }



    return 0;
}
