//
// Created by User on 11/28/2023.
//
#include "stdio.h"

int selection_sort(int a[],int n){

    int min,temp,j,i;
    for( i = 0;i<n;i++){
        min = i;
        j = i+1;
        while(j < n){
            if(a[j]< a[min]){
                min = j;
            }j++;
        }
        if( i != min){
            temp = a[i];
            a[i] = a[min];
            a[min] = temp;
        }
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

    a[n] = selection_sort(a,n);

    for(i = 0;i<n;i++){
        printf("%d\t",a[i]);
    }


    return 0;
}