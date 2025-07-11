//
// Created by User on 9/13/2023.
//the a[] in the function definition acts as a pointer to the initial base address of the array passed into the function
// hence in essence it is still call by reference
#include "stdio.h"

int sum = 0;
int avg(int a[],int x){
    for(int i = 0;i< x;i++){
        sum += a[i];
    }
    return sum / x;
}

int main(){
    int marks[5],i,x;
    int len = sizeof (marks)/ sizeof (int);

    for(i = 0;i<len;i++){
        printf("Enter the marks of students: ");
        scanf("%d",&marks[i]);
    }

    x = avg(marks,len);
    printf("\nThe avg value of students is %d",x);


   return 0;
}
