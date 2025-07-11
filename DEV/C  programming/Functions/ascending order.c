//
// Created by User on 7/2/2023.
//Write a C program to sort an integer array in ascending order using the Bubble Sort algorithm.


#include <stdio.h>


int main(){
    int i,k,j;
    int a[5] = {100,24,200,38,45};
    int len = sizeof(a)/sizeof(int);


    //bubble sorting the array
    for(j = 0;j<len;j++){
        for(i = 0;i<len;i++){
            if(a[i]>a[i+1]){
                int c = a[i];
                a[i] = a[i+1];
                a[i+1] = c;
            }
        }
    }

    for(k = 0;k<len;k++){
        printf("%d ",a[k]);
    }


    return 0;
}
