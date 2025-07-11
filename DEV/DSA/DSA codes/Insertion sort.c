//
// Created by User on 11/27/2023.
//
#include "stdio.h"




int insertion_sort(int a[],int n){
    int i,j,temp;
    for(i = 1;i<n;i++){
        temp = a[i];
        j = i-1;
        while( a[j] > temp && j >= 0){
            a[j+1] = a[j];
            j--;
        }
        a[j+1] = temp;
    }


    return a[i];
}

int main(){
    int n,i;
    printf("Enter the number of array elements: ");
    scanf("%d",&n);
    int a[n];

    for(i = 0;i<n;i++){
        printf("Enter a[%d]: ",i);
        scanf("%d",&a[i]);
    }

    a[n] = insertion_sort(a,n);

    for(i = 0;i<n;i++){
        printf("%d\t",a[i]);
    }


    return 0;
}