//
// Created by User on 6/29/2023.
//Problem: Write a function that takes an array of integers and its size as parameters,
// and returns the sum of all the elements in the array.

#include <stdio.h>
int marks[10];
int n = sizeof(marks)/sizeof(int);

// this a void function
void creating_arrays(){
    int j;
    // getting user to create the array for the marks
    for(j = 0;j<n;j++){
        printf("Enter marks of student: ");
        scanf("%d",&marks[j]);
    }

}
// this is a value returning function
int sum_of_marks( int arr[],int len){
    int i,sum = 0;
    for(i = 0;i<len;i++){
        sum += arr[i];
    }
    return sum;
}


int main(){
    creating_arrays();
    printf("Sum of marks: %d", sum_of_marks(marks,n));

    return 0;
}